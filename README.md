# Fast-Soy-Admin (企业级纯净开发版)

**Fast-Soy-Admin** 是一款基于 **FastAPI** 与 **Soybean Admin** 构建的高性能、全栈后台管理系统脚手架。本项目旨在为工业自动化、B2B 贸易及企业级中后台应用提供一个极简、纯净、安全的开发底座。

---

## 🌟 项目特色

* **全栈异步设计**：后端采用 FastAPI + Tortoise ORM 的全异步架构，轻松应对高并发场景。
* **极致纯净**：已彻底剥离所有演示性外链（如官方文档 iframe）、冗余视图及危险的 Demo 定时重置脚本，确保代码库可以直接用于生产环境。
* **企业级权限系统**：内置完整的用户 (User)、角色 (Role)、菜单 (Menu)、接口 (API) 及日志 (Log) 管理模块。
* **现代前端生态**：前端基于 Vue 3 + Vite + Naive UI，集成 Elegant Router 自动化路由方案及 UnoCSS 原子化 CSS。
* **前后端分离架构 (Monorepo)**：前端与后端独立运作，互不干扰，配合单体仓库提升维护效率。

---

## 📂 项目结构

```text
fast-soy-admin/
├── admin-backend/          # 后端核心代码 (FastAPI / Python)
├── admin-frontend/         # 前端核心代码 (Vue3 / TypeScript)
├── docker-compose.yml      # 全局容器编排配置 (可选，如需统一部署)
├── LICENSE                 # 开源许可协议
└── README.md               # 项目全局说明文档 (本文档)
```

---

## 🚀 快速开始

本项目为清晰的前后端解耦架构，本地开发时，需要分别进入对应目录启动服务。

### 1. 启动后端 (Backend Service)
进入 `admin-backend` 目录，配置数据库并启动 FastAPI 服务。
👉 **[点击查看后端启动文档](./admin-backend/README.md)**

### 2. 启动前端 (Frontend UI)
进入 `admin-frontend` 目录，安装 Node 依赖并启动 Vite 界面。
👉 **[点击查看前端启动文档](./admin-frontend/README.md)**

---

## 📄 许可证
本项目遵循 [MIT](./LICENSE) 开源协议。
