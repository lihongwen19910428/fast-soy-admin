# Fast-Soy-Admin - Backend (后端API服务)

这是 Fast-Soy-Admin 项目的纯后端服务代码库，核心基于 **FastAPI** 现代异步框架构建。

## 🛠️ 技术栈

* **框架**: [FastAPI](https://fastapi.tiangolo.com/) - 现代、快速（高性能）的 Python Web 框架。
* **ORM**: [Tortoise ORM](https://tortoise-orm.readthedocs.io/) - 受 Django 启发的全异步映射库。
* **认证**: JWT (PyJWT) - 基于 Token 的安全身份验证。
* **日志**: Loguru - 简洁高效的日志管理。
* **数据校验**: Pydantic v2 - 强大的数据序列化与验证。

## 📂 后端目录结构

```text
admin-backend/
├── app/                    # 后端核心代码
│   ├── api/v1/             # RESTful 接口路由层
│   ├── controllers/        # 业务逻辑处理层
│   ├── core/               # 核心能力 (异常处理、中间件、Redis等)
│   ├── models/system/      # 数据库模型定义 (Tortoise ORM)
│   ├── schemas/            # Pydantic 数据传输与验证模型
│   └── settings/           # 系统配置解析获取
├── deploy/                 # Docker 部署相关配置
├── .env                    # 系统环境变量
├── requirements.txt        # PIP 经典依赖列表
├── uv.lock/pdm.lock        # 新一代包引擎锁文件
└── run.py                  # 服务启动入口
```

## 🚀 快速启动

### 1. 配置环境变量
如果你刚 clone 下来，请在 `admin-backend` 根目录下，将 `.env.example` 复制或修改为 `.env`，填入你本地的数据库连接信息：
```bash
# 打开 .env 文件，修改类似这样的 MySQL/Redis URL：
DB_URL=mysql://root:password@127.0.0.1:3306/fast_soy_admin
```

### 2. 安装依赖并运行

**如果你习惯使用原生的 pip (通过 venv 虚拟环境)：**
```bash
pip install -r requirements.txt
python run.py
```

**如果你使用现代化的包管理工具 uv（推荐）：**
```bash
uv sync
uv run run.py
```

服务启动后：
- 默认监听：`http://127.0.0.1:8000` (或 `localhost`)
- 接口文档 (Swagger UI)：访问 `http://127.0.0.1:8000/docs` 便可进行接口测试。