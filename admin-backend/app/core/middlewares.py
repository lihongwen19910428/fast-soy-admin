from uuid import uuid4
from datetime import datetime
from json import JSONDecodeError

import orjson
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.types import ASGIApp, Receive, Scope, Send

from app.core.bgtask import BgTasks
from app.core.code import Code
from app.core.ctx import CTX_X_REQUEST_ID, CTX_USER_ID
from app.core.dependency import check_token
from app.core.exceptions import HTTPException
from app.models.system import LogType
from app.models.system import User, Log, APILog
from app.settings import APP_SETTINGS


class SimpleBaseMiddleware:
    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http":
            await self.app(scope, receive, send)
            return

        await self.handle_http(scope, receive, send)

    async def handle_http(self, scope, receive, send) -> None:
        request = Request(scope, receive)
        response = await self.before_request(request) or self.app

        async def send_wrapper(_response):
            await self.after_request(request, _response)
            await send(_response)

        await response(scope, receive, send_wrapper)

    async def before_request(self, request: Request) -> ASGIApp | None:
        ...

    async def after_request(self, request: Request, response: dict):
        ...


class BackGroundTaskMiddleware(SimpleBaseMiddleware):
    async def before_request(self, request: Request) -> ASGIApp | None:
        await BgTasks.init_bg_tasks_obj()
        return self.app

    async def after_request(self, request: Request, response: dict) -> None:
        if response.get("type") == "http.response.body" and not response.get("more_body", False):
            await BgTasks.execute_tasks()



async def create_api_log(log_data: dict, user_id: int | None, x_request_id: str):
    user_obj = await User.filter(id=user_id).first() if user_id else None
    api_log_obj = await APILog.create(**log_data)
    await Log.create(log_type=LogType.ApiLog, by_user=user_obj, api_log=api_log_obj, x_request_id=x_request_id)
    return api_log_obj.id


async def update_api_log(api_log_id: int, response_data: dict, process_time: float):
    api_log_obj = await APILog.get_or_none(id=api_log_id)
    if api_log_obj:
        api_log_obj.response_data = response_data
        api_log_obj.response_code = str(response_data.get("code", "-1"))
        api_log_obj.process_time = process_time
        await api_log_obj.save()


class APILoggerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request.state.start_time = datetime.now()
        path = request.url.path
        x_request_id = uuid4().hex
        CTX_X_REQUEST_ID.set(x_request_id)
        request.state.x_request_id = x_request_id

        # Determine if logging is needed
        should_log = (
            all([exclude not in path for exclude in APP_SETTINGS.ADD_LOG_ORIGINS_DECLUDE])
            and (
                "*" in APP_SETTINGS.ADD_LOG_ORIGINS_INCLUDE
                or any([include in path for include in APP_SETTINGS.ADD_LOG_ORIGINS_INCLUDE]))
        )

        if should_log and request.scope["type"] == "http":
            token = request.headers.get("Authorization")
            user_id = None
            if token:
                status, _, decode_data = check_token(token.replace("Bearer ", "", 1))
                if status and decode_data:
                    user_id = int(decode_data["data"]["userId"])
                    CTX_USER_ID.set(user_id)

            try:
                # Use a wrapper or clone if needed, but for now just read
                request_data = await request.json() if request.method in ["POST", "PUT", "PATCH"] else None
            except (JSONDecodeError, UnicodeDecodeError):
                request_data = None

            url_path = request.url.path
            if len(url_path) > 500:
                raise HTTPException(msg="请求url path过长, 请联系开发人员", code=Code.FAIL)

            api_log_data = dict(
                ip_address=request.client.host if request.client else None,
                user_agent=request.headers.get("user-agent"),
                request_domain=request.url.hostname,
                request_path=url_path,
                request_params=dict(request.query_params) or None,
                request_data=request_data,
                x_request_id=x_request_id,
            )

            # We need the ID for the response middleware, so we might still need to create it synchronously
            # OR we can pass a future/context.
            # To keep it simple and correct for ID tracking, we create APILog synchronously but Log and relations can be background.
            # Actually, let's just move the whole thing to background and use x_request_id to link if needed.
            # But the current design expects request.state.api_log_id.
            
            api_log_obj = await APILog.create(**api_log_data)
            request.state.api_log_id = api_log_obj.id
            
            # Background task for the Log entry and User relation
            await BgTasks.add_task(Log.create, log_type=LogType.ApiLog, by_user_id=user_id, api_log=api_log_obj, x_request_id=x_request_id)

        response = await call_next(request)
        return response


class APILoggerAddResponseMiddleware(SimpleBaseMiddleware):
    async def after_request(self, request: Request, response: dict) -> None:
        if response.get("type") == "http.response.body" and hasattr(request.state, "api_log_id"):
            response_body = response.get("body", b"")
            try:
                resp = orjson.loads(response_body)
                process_time = (datetime.now() - request.state.start_time).total_seconds()
                # Move update to background
                await BgTasks.add_task(update_api_log, request.state.api_log_id, resp, process_time)
            except (orjson.JSONDecodeError, UnicodeDecodeError):
                ...

        if response.get("type") == "http.response.start" and hasattr(request.state, "x_request_id"):
            response["headers"].append((b"x-request-id", request.state.x_request_id.encode()))

