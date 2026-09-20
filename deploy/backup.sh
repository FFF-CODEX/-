#!/usr/bin/env bash

set -euo pipefail

PROJECT_DIR="${PROJECT_DIR:-/opt/weizhu}"
BACKUP_DIR="${BACKUP_DIR:-${PROJECT_DIR}/backups}"
ENV_FILE="${ENV_FILE:-${PROJECT_DIR}/.env.production}"
RETENTION_DAYS="${RETENTION_DAYS:-30}"

mkdir -p "${BACKUP_DIR}"

timestamp="$(date +%Y%m%d-%H%M%S)"
database_backup="${BACKUP_DIR}/database-${timestamp}.sql.gz"

cd "${PROJECT_DIR}"

docker compose --env-file "${ENV_FILE}" exec -T db \
  sh -c 'pg_dump -U "$POSTGRES_USER" "$POSTGRES_DB"' \
  | gzip > "${database_backup}"

find "${BACKUP_DIR}" -type f -name 'database-*.sql.gz' \
  -mtime "+${RETENTION_DAYS}" -delete

printf '数据库备份完成: %s\n' "${database_backup}"
