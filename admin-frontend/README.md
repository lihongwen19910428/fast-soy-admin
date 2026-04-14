这份为您定制的详细 `README.md` 结合了您提供的代码结构、技术栈以及我们之前讨论的“代码净化”方案。它不仅展示了项目的核心价值，还为开发者提供了清晰的指引。

---

# Fast-Soy-Admin (企业级纯净开发版)

**Fast-Soy-Admin** 是一款基于 **FastAPI** 与 **Soybean Admin** 构建的高性能、全栈后台管理系统脚手架。本项目旨在为工业自动化、B2B 贸易及企业级中后台应用提供一个极简、纯净、安全的开发底座。

---

## 🌟 项目特色

* **全栈异步设计**：后端采用 FastAPI + Tortoise ORM 的全异步架构，轻松应对高并发场景。
* **极致纯净**：已彻底剥离所有演示性外链（如官方文档 iframe）、冗余视图及危险的 Demo 定时重置脚本，确保代码库可以直接用于生产环境。
* **企业级权限系统**：内置完整的用户 (User)、角色 (Role)、菜单 (Menu)、接口 (API) 及日志 (Log) 管理模块。
* **现代前端生态**：前端基于 Vue 3 + Vite + Naive UI，集成 Elegant Router 自动化路由方案及 UnoCSS 原子化 CSS。
* **工业级适配**：针对 Li Hongwen 关注的工业自动化与 B2B 场景，优化了数据处理效率与 UI 交互体验。

---

## 🛠️ 技术栈

### 后端 (Python)
* **框架**: [FastAPI](https://fastapi.tiangolo.com/) - 现代、快速（高性能）的 Python Web 框架。
* **ORM**: [Tortoise ORM](https://tortoise-orm.readthedocs.io/) - 受 Django 启发的异步 ORM。
* **认证**: JWT (PyJWT) - 基于 Token 的安全身份验证。
* **日志**: Loguru - 简洁高效的日志管理。
* **数据校验**: Pydantic v2 - 强大的数据序列化与验证。

### 前端 (Vue3)
* **核心**: Vue 3.4+ & TypeScript。
* **构建**: Vite 5+ - 极速的热更新与构建体验。
* **UI 组件**: [Naive UI](https://www.naiveui.com/) - 优雅的 Vue3 组件库。
* **路由**: Elegant Router - 自动化路由插件，提升开发效率。
* **CSS**: UnoCSS - 高性能、按需加载的原子化 CSS 引擎。
* **请求**: Alova & Axios 双支持，默认采用 Alova 实现轻量级请求管理。

---

## 📂 项目结构

```text
fast-soy-admin/
├── app/                    # 后端核心代码
│   ├── api/v1/             # RESTful 接口路由层 (Auth, User, Role, Menu, API, Log)
│   ├── controllers/        # 业务逻辑处理层
│   ├── core/               # 核心能力 (异常处理、中间件、Redis、初始化)
│   ├── models/system/      # 数据库模型定义 (Tortoise ORM)
│   ├── schemas/            # Pydantic 数据传输模型
│   └── settings/           # 系统配置文件 (数据库、JWT、CORS 等)
├── web/                    # 前端核心代码
│   ├── build/              # Vite 插件及构建配置
│   ├── packages/           # 内部公共包 (hooks, utils, axios, alova, materials)
│   ├── src/                # 源代码
│   │   ├── layouts/        # 全局布局 (Base, Blank, Sider, Header, Tab)
│   │   ├── service/        # API 请求定义
│   │   ├── store/          # Pinia 状态管理
│   │   └── views/          # 业务视图页面 (Manage, UserCenter, Exception)
│   └── vite.config.ts      # 前端构建核心配置
├── deploy/                 # Docker 部署方案
├── docker-compose.yml      # 容器编排配置
└── run.py                  # 后端入口启动文件
```

---

## 🛡️ 净化说明 (Pure Version)

本项目已移除原版脚手架中不适合商业环境的代码：
1.  **移除 `cron_reset.py`**：禁止在开发或生产环境中自动定时清空数据库，保障数据安全。
2.  **精简前端路由**：在 `web/src/router/routes/index.ts` 中剔除了所有 `document` 相关的第三方演示外链，使侧边栏和路由表回归业务本质。
3.  **剔除 Demo 视图**：移除了大量的样式演示页面，保留了 `manage` 核心管理视图，开发者可直接在此基础上扩展业务。

---

## 🚀 快速开始

### 1. 后端准备 (App)
```bash
# 进入后端目录 (假设已安装 Python 3.10+)
# 安装依赖
pip install -r requirements.txt

# 配置环境变量
cp .env.example .env  # 根据实际情况修改数据库连接

# 启动服务
python run.py
```

### 2. 前端准备 (Web)
```bash
cd web

# 安装依赖 (推荐使用 pnpm)
pnpm install

# 启动开发服务器
pnpm dev
```
访问地址：`http://localhost:9527` (默认)。

---

## 🐳 部署 (Docker)
项目已预置 Docker 化方案：
```bash
# 启动全栈服务 (FastAPI + Vue + MySQL + Redis)
docker-compose up -d
```
Docker 配置涵盖了多阶段构建，确保镜像体积最小化。

---

## 📄 许可证
本项目遵循 [MIT](./LICENSE) 开源协议。