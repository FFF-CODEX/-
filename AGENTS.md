# AGENTS.md

## 项目概述

本项目是"小李外贸"业务平台，采用前后端分离架构：

- 后端：Django 6.1，运行在 Python 3.12.10 虚拟环境（`.venv`）
- 后台管理：Django Admin + SimpleUI（默认中文界面）
- 前台：Vue 3 + Vite，构建产物由 Django 直接托管

## 目录结构

```text
config/       Django 项目配置（settings、urls、wsgi、asgi）
core/         Django 应用，提供前台页面入口和 API 接口
frontend/     Vue 3 前端工程（src 源码、dist 构建产物）
.venv/        Python 虚拟环境
manage.py     Django 管理入口
requirements.txt  Python 依赖清单
```

## 常用命令

### 后端

```powershell
# 激活虚拟环境
.\.venv\Scripts\Activate.ps1

# 启动 Django 开发服务器
python manage.py runserver

# 运行系统检查
python manage.py check

# 应用数据库迁移
python manage.py migrate
```

### 前端

```powershell
# 进入前端目录
cd frontend

# 安装依赖
npm install

# 前端开发模式（默认端口 5173，/api 代理到 8000）
npm run dev

# 构建生产产物（构建后 8000 端口才会展示最新页面）
npm run build
```

## 关键约定

- 后台地址为 `/admin/`，前台根路径 `/` 返回 `frontend/dist/index.html`。
- Django 通过 `/api/` 提供数据接口，当前接口为 `GET /api/`。
- 前端修改源码后必须重新执行 `npm run build`，Django 托管的页面才会更新。
- 前端开发调试使用 Vite 的 5173 端口，接口请求会代理到 Django 8000 端口。
- 新增 Python 依赖后同步更新 `requirements.txt`；新增前端依赖后更新 `frontend/package.json`。
- 代码注释统一使用中文。
