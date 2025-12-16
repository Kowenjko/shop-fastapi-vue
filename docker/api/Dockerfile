# docker/api/Dockerfile (dev)
FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Устанавливаем uv (менеджер зависимостей) и pip-tools если нужно
RUN apt-get update && apt-get install -y --no-install-recommends build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade pip wheel uv

# Копируем описания зависимостей (для кэширования)
COPY api/pyproject.toml api/uv.lock* /app/

# Синхронизируем зависимости (создаст .venv внутри контейнера)s
RUN uv sync --no-dev || true

# Копируем приложение (в dev мы монтируем ./api, но COPY даёт базовую копию)
COPY api/ /app/

RUN chmod +x prestart.sh

# expose
EXPOSE 8000

# Запуск: используем python run.py (в dev run.py должен учитывать DEV)
CMD ["./prestart.sh"]
CMD ["uv", "run", "python", "run.py"]
