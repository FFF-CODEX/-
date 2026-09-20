# 微筑工坊

基于 Django 6.1 和 Vue 3 的高铁工程缩微模型展示与业务咨询网站。

## 项目结构

```text
config/       Django 项目配置
core/         Django 应用、数据模型和接口
frontend/     Vue 3 前端源码
manage.py     Django 管理入口
```

## 本地开发

后端：

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

前端：

```powershell
cd frontend
npm install
npm run dev
```

前端地址为 `http://127.0.0.1:5173`，`/api` 请求会代理到 Django 的 8000 端口。

## 生产构建

```powershell
cd frontend
npm run build
```

Django 会从 `frontend/dist/index.html` 提供前端页面，静态资源统一使用 `/static/` 路径。

## 环境变量

生产环境至少需要配置：

```text
DJANGO_SECRET_KEY
DJANGO_DEBUG
DJANGO_ALLOWED_HOSTS
DJANGO_CSRF_TRUSTED_ORIGINS
DJANGO_ACCESS_CODE
```

可以参考 `.env.example`。真实的 `.env`、`.env.production` 和数据库文件禁止提交到 GitHub。

## GitHub 上传范围

需要提交：

- `manage.py`
- `requirements.txt`
- `config/`
- `core/`
- `frontend/package.json`
- `frontend/package-lock.json`
- `frontend/vite.config.js`
- `frontend/index.html`
- `frontend/public/`
- `frontend/src/`
- `frontend/.vscode/extensions.json`（可选）
- `AGENTS.md`（可选）
- `README.md`
- `.gitignore`
- `.env.example`

不需要提交：

- `.venv/`
- `frontend/node_modules/`
- `frontend/dist/`
- `frontend/public/images/` 中当前未使用的冗余图片
- `db.sqlite3`
- `__pycache__/` 和 `*.pyc`
- `照片库/`
- `logo-preview.html`
- 真实环境变量文件、日志和上传文件目录
