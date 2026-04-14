# Fast-Soy-Admin - Frontend (前端交互界面)

这是 Fast-Soy-Admin 项目的前端用户界面，基于高度定制与企业级净化后的 [Soybean Admin](https://github.com/soybeanjs/soybean-admin) 开发。

## 🛠️ 技术栈

* **核心**: Vue 3.4+ & TypeScript。
* **构建**: Vite 5+ - 极速的热更新与构建打包体验。
* **UI 组件**: [Naive UI](https://www.naiveui.com/) - 优雅的 Vue3 组件库。
* **路由**: Elegant Router - 自动化路由插件，提升开发效率。
* **CSS**: UnoCSS - 高性能、按需加载的原子化 CSS 引擎。
* **请求与状态**: Alova/Axios 进行网络请求，Pinia 进行状态管理。

## 📂 前端目录结构

```text
admin-frontend/
├── src/                    # 源代码
│   ├── layouts/            # 全局布局 (Header顶栏, Sider侧边栏等)
│   ├── service/            # API 接口请求与定义
│   ├── store/              # Pinia 状态树
│   └── views/              # 开发的所有路由视图与页面
├── .env                    # 环境变量 (代理接口路径配置)
├── package.json            # 依赖包及 Node.js 脚本
└── vite.config.ts          # Vite 构建核心配置
```

## 🚀 快速启动

### 1. 前置要求
- 需要安装 `Node.js` (建议 v18.x 或更高版本)。
- 虽然可以使用 npm/npm，但本项目强制推荐使用 `pnpm` 作为包管理器。

### 2. 检查应用环境映射
在运行前，请检查项目下的 `.env` (或对应环境如 `.env.test`, `.env.prod`) 中关于接口网关的代理是否正确：
通常会自动通过 Vite 将接口打向后端的 `http://localhost:8000`。

### 3. 安装依赖及运行项目

进入到 `admin-frontend` 目录下，在终端中依次执行：
```bash
# 1. 安装项目所有相关前端依赖包 (如果未安装pnpm可先执行 npm install -g pnpm)
pnpm install

# 2. 启动开发服务器
pnpm dev
```

成功后，控制台会输出本地访问路径。通过浏览器访问 (通常是 `http://localhost:9527`) 即可打开系统界面。