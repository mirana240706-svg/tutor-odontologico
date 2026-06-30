#!/bin/sh
set -e
echo "Esperando a PostgreSQL..."
while ! nc -z postgres 5432; do
  sleep 1
done
echo "PostgreSQL listo."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
