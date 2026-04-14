from pathlib import Path
from typing import Any

from pydantic_settings import BaseSettings
from pydantic import Field
import secrets


def tortoise_orm_factory() -> dict[str, Any]:
    return {
        "connections": {
            "conn_system": {
                "engine": "tortoise.backends.sqlite",
                "credentials": {"file_path": "app_system.sqlite3"}
            }
        },
        "apps": {
            "app_system": {"models": ["app.models.system", "aerich.models"], "default_connection": "conn_system"}
        },
        "use_tz": False,
        "timezone": "Asia/Shanghai"
    }


class Settings(BaseSettings):
    VERSION: str = "0.1.0"
    APP_TITLE: str = "FastSoyAdmin"
    APP_DESCRIPTION: str = "Description"

    # CORS_ORIGINS: list[str] = Field(default_factory=lambda: ["*"])
    # CORS_ALLOW_CREDENTIALS: bool = True
    # 修改后 (推荐写法，用正则允许所有跨域，且兼容 credentials=True)
    CORS_ORIGIN_REGEX: str = ".*"  # 允许所有源跨域
    CORS_ALLOW_CREDENTIALS: bool = True
    CORS_ALLOW_METHODS: list[str] = Field(default_factory=lambda: ["*"])
    CORS_ALLOW_HEADERS: list[str] = Field(default_factory=lambda: ["*"])

    ADD_LOG_ORIGINS_INCLUDE: list[str] = Field(default_factory=lambda: ["*"])
    ADD_LOG_ORIGINS_DECLUDE: list[str] = Field(default_factory=lambda: ["/system-manage", "/redoc", "/doc", "/openapi.json"])

    DEBUG: bool = False

    PROJECT_ROOT: Path = Path(__file__).resolve().parent.parent
    BASE_DIR: Path = PROJECT_ROOT.parent
    LOGS_ROOT: Path = BASE_DIR / "logs/"
    STATIC_ROOT: Path = BASE_DIR / "static/"
    # 方案：无环境变量时自动生成随机值，确保绝对安全
    SECRET_KEY: str = Field(default_factory=lambda: secrets.token_hex(32))
    JWT_ALGORITHM: str = "HS256"
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 12  # 12 hours
    JWT_REFRESH_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days

    TORTOISE_ORM: dict[str, Any] = Field(default_factory=tortoise_orm_factory)

    DATETIME_FORMAT: str = "%Y-%m-%d %H:%M:%S"

    REDIS_URL: str = "redis://redis:6379/0"  # "redis://:password@233.233.233.233:33333/0"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        extra = "ignore"


settings = Settings()
