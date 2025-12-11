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
# DEV HTTPS CERTIFICATES
# --------------------------

dev-certs:
	mkdir -p nginx/certs nginx/ca
	@echo "==> Creating root CA..."
	openssl genrsa -out nginx/ca/rootCA.key 4096
	openssl req -x509 -new -nodes -key nginx/ca/rootCA.key -sha256 -days 1024 -out nginx/ca/rootCA.crt -subj "/CN=Dev Root CA"

	@echo "==> Creating $(CLIENT_URL) certificate..."
	openssl genrsa -out nginx/certs/$(CLIENT_URL).key 2048
	openssl req -new -key nginx/certs/$(CLIENT_URL).key -out nginx/certs/$(CLIENT_URL).csr -subj "/CN=$(CLIENT_URL)"
	echo "subjectAltName = DNS:$(CLIENT_URL)" > nginx/certs/$(CLIENT_URL).ext
	openssl x509 -req -in nginx/certs/$(CLIENT_URL).csr -CA nginx/ca/rootCA.crt -CAkey nginx/ca/rootCA.key -CAcreateserial -out nginx/certs/$(CLIENT_URL).crt -days 365 -sha256 -extfile nginx/certs/$(CLIENT_URL).ext

	@echo "==> Creating $(API_URL) certificate..."
	openssl genrsa -out nginx/certs/$(API_URL).key 2048
	openssl req -new -key nginx/certs/$(API_URL).key -out nginx/certs/$(API_URL).csr -subj "/CN=$(API_URL)"
	echo "subjectAltName = DNS:$(API_URL)" > nginx/certs/$(API_URL).ext
	openssl x509 -req -in nginx/certs/$(API_URL).csr -CA nginx/ca/rootCA.crt -CAkey nginx/ca/rootCA.key -CAcreateserial -out nginx/certs/$(API_URL).crt -days 365 -sha256 -extfile nginx/certs/$(API_URL).ext

	@echo "==> Adding root CA to Ubuntu trusted certificates..."
	sudo cp nginx/ca/rootCA.crt /usr/local/share/ca-certificates/dev-root-ca.crt
	sudo update-ca-certificates

	@echo "✅ Dev certificates created in nginx/certs and installed!"

# --------------------------
# DATABASE MIGRATIONS (ALEMBIC)
# --------------------------
# make revision msg="description"
# make migrate
# make downgrade

revision:
	@if [ -z "$(msg)" ]; then \
		echo "⚠️ Usage: make revision msg=\"description\""; \
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
