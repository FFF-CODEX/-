# 生产部署

项目使用 Docker Compose 运行 Django、PostgreSQL、Nginx 和 Cloudflare Tunnel。

## 服务器要求

```text
Ubuntu 22.04 或 24.04
2 核 CPU
2GB 内存
40GB 以上磁盘
```

## Cloudflare Tunnel

在 Cloudflare Zero Trust 中创建 Tunnel，并添加 Public Hostname：

```text
Subdomain: model
Domain: 你的域名
Service Type: HTTP
URL: nginx:80
```

复制 Tunnel Token，写入服务器 `.env.production`。

## 环境变量

在项目根目录创建 `.env.production`：

```env
DJANGO_SECRET_KEY=随机生成的长密钥
DJANGO_DEBUG=0
DJANGO_ALLOWED_HOSTS=model.example.com
DJANGO_CSRF_TRUSTED_ORIGINS=https://model.example.com
DJANGO_ACCESS_CODE=比赛访问码
DJANGO_TIME_ZONE=Asia/Shanghai
ENABLE_ACCESS_GUARD=True

POSTGRES_DB=weizhu
POSTGRES_USER=weizhu
POSTGRES_PASSWORD=强数据库密码
POSTGRES_HOST=db
POSTGRES_PORT=5432

CLOUDFLARE_TUNNEL_TOKEN=Cloudflare Token
```

## 启动

```bash
docker compose --env-file .env.production up -d --build
docker compose exec web python manage.py createsuperuser
docker compose ps
```

`web` 容器启动时会自动执行数据库迁移和静态文件收集。

## 更新

```bash
git pull
docker compose --env-file .env.production up -d --build
```

## 备份

```bash
chmod +x deploy/backup.sh
./deploy/backup.sh
```

建议每天通过 cron 执行备份，并把备份同步到 Cloudflare R2。
