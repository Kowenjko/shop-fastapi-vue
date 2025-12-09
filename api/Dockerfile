FROM python:3.12.6-bookworm

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

RUN pip install --upgrade pip wheel "uv"

# RUN poetry config virtualenvs.create false

COPY backend/pyproject.toml backend/uv.lock ./

RUN uv sync

COPY backend .

# RUN chmod +x prestart.sh
# RUN chmod +x run

# ENTRYPOINT ["./prestart.sh"]
CMD ["uv", "run", "python", "run.py"]
