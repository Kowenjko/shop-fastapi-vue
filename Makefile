SHELL := /bin/bash

DEV_COMPOSE = docker compose
API = $(DEV_COMPOSE) exec api

CLIENT_URL = shop.local
API_URL = api.shop.local

# --------------------------
# DEV COMMANDS
# --------------------------

dev:
	$(DEV_COMPOSE) up --build

down:
	$(DEV_COMPOSE) down

up:
	$(DEV_COMPOSE) up -d

restart:
	$(DEV_COMPOSE) down
	$(DEV_COMPOSE) up --build

logs:
	$(DEV_COMPOSE) logs -f

clean:
	docker system prune -af --volumes


# --------------------------
# SSL CERTIFICATES
# --------------------------

certs:
	mkdir -p nginx/certs
	openssl req -x509 -nodes -days 365 \
		-newkey rsa:2048 \
		-keyout nginx/certs/$(CLIENT_URL).key \
		-out nginx/certs/$(CLIENT_URL).crt \
		-subj "/CN=$(CLIENT_URL)"

	openssl req -x509 -nodes -days 365 \
		-newkey rsa:2048 \
		-keyout nginx/certs/$(API_URL).key \
		-out nginx/certs/$(API_URL).crt \
		-subj "/CN=$(API_URL)"


# --------------------------
# DATABASE MIGRATIONS (ALEMBIC)
# --------------------------
# make revision msg="add users table"
# make migrate

revision:
	@if [ -z "$(msg)" ]; then \
		echo "⚠️  Usage: make revision msg=\"description\""; \
		exit 1; \
	fi
	$(API) alembic revision --autogenerate -m "$(msg)"

migrate:
	$(API) alembic upgrade head

downgrade:
	$(API) alembic downgrade -1


# --------------------------
# SEED DATABASE
# --------------------------
# make seed
# --------------------------

seed:
	$(API) uv run python run_seed.py


# --------------------------
# PROD COMMANDS
# --------------------------

prod:
	$(DEV_COMPOSE) -f docker-compose.prod.yml up --build -d

prod-down:
	$(DEV_COMPOSE) -f docker-compose.prod.yml down
