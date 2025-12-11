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
# ROOT CA + DEV CERTIFICATES
# --------------------------

dev-certs:
	mkdir -p nginx/certs nginx/ca

	@echo "==> Creating ROOT CA using nginx/rootCA.conf..."
	openssl genrsa -out nginx/ca/rootCA.key 4096
	openssl req -x509 -new -nodes \
		-key nginx/ca/rootCA.key \
		-sha256 -days 1024 \
		-out nginx/ca/rootCA.crt \
		-config nginx/rootCA.conf

	@echo "==> Creating certificate for $(CLIENT_URL)..."
	openssl genrsa -out nginx/certs/$(CLIENT_URL).key 2048
	openssl req -new -key nginx/certs/$(CLIENT_URL).key \
		-out nginx/certs/$(CLIENT_URL).csr \
		-subj "/CN=$(CLIENT_URL)"
	echo "subjectAltName = DNS:$(CLIENT_URL)" > nginx/certs/$(CLIENT_URL).ext
	openssl x509 -req \
		-in nginx/certs/$(CLIENT_URL).csr \
		-CA nginx/ca/rootCA.crt \
		-CAkey nginx/ca/rootCA.key \
		-CAcreateserial \
		-out nginx/certs/$(CLIENT_URL).crt \
		-days 365 -sha256 \
		-extfile nginx/certs/$(CLIENT_URL).ext

	@echo "==> Creating certificate for $(API_URL)..."
	openssl genrsa -out nginx/certs/$(API_URL).key 2048
	openssl req -new -key nginx/certs/$(API_URL).key \
		-out nginx/certs/$(API_URL).csr \
		-subj "/CN=$(API_URL)"
	echo "subjectAltName = DNS:$(API_URL)" > nginx/certs/$(API_URL).ext
	openssl x509 -req \
		-in nginx/certs/$(API_URL).csr \
		-CA nginx/ca/rootCA.crt \
		-CAkey nginx/ca/rootCA.key \
		-CAcreateserial \
		-out nginx/certs/$(API_URL).crt \
		-days 365 -sha256 \
		-extfile nginx/certs/$(API_URL).ext

	@echo "==> Installing Root CA into Ubuntu trusted system certificates..."
	sudo cp nginx/ca/rootCA.crt /usr/local/share/ca-certificates/dev-root-ca.crt
	sudo update-ca-certificates

	@echo "✅ Dev certificates created and installed!"


# --------------------------
# MANUAL DOMAIN CERTIFICATE
# Usage: make cert DOMAIN=my.local
# --------------------------

cert:
ifndef DOMAIN
	$(error ❌ DOMAIN is not set! Use: make cert DOMAIN=example.local)
endif
	@echo "==> Creating certificate for $(DOMAIN)..."

	mkdir -p nginx/certs

	openssl genrsa -out nginx/certs/$(DOMAIN).key 2048

	openssl req -new \
		-key nginx/certs/$(DOMAIN).key \
		-out nginx/certs/$(DOMAIN).csr \
		-subj "/CN=$(DOMAIN)"

	echo "subjectAltName = DNS:$(DOMAIN)" > nginx/certs/$(DOMAIN).ext

	openssl x509 -req \
		-in nginx/certs/$(DOMAIN).csr \
		-CA nginx/ca/rootCA.crt \
		-CAkey nginx/ca/rootCA.key \
		-CAcreateserial \
		-out nginx/certs/$(DOMAIN).crt \
		-days 365 -sha256 \
		-extfile nginx/certs/$(DOMAIN).ext

	@echo "✅ Certificate created: $(DOMAIN)"


# --------------------------
# SAN CERTIFICATE
# Usage:
#   make san DOMAIN=site.local ALT="a.site.local b.site.local"
# --------------------------

san:
ifndef DOMAIN
	$(error ❌ DOMAIN is not set! Use: make san DOMAIN=site.local ALT="a.site.local b.site.local")
endif
ifndef ALT
	$(error ❌ ALT is not set! Use: make san DOMAIN=site.local ALT="a.site.local b.site.local")
endif

	@echo "==> Creating SAN certificate for $(DOMAIN) with: $(ALT)"

	mkdir -p nginx/certs

	openssl genrsa -out nginx/certs/$(DOMAIN).key 2048

	openssl req -new \
		-key nginx/certs/$(DOMAIN).key \
		-out nginx/certs/$(DOMAIN).csr \
		-subj "/CN=$(DOMAIN)"

	@echo "subjectAltName = DNS:$(DOMAIN)" > nginx/certs/$(DOMAIN).ext
	@for d in $(ALT); do \
		echo ", DNS:$$d" >> nginx/certs/$(DOMAIN).ext; \
	done

	openssl x509 -req \
		-in nginx/certs/$(DOMAIN).csr \
		-CA nginx/ca/rootCA.crt \
		-CAkey nginx/ca/rootCA.key \
		-CAcreateserial \
		-out nginx/certs/$(DOMAIN).crt \
		-days 365 -sha256 \
		-extfile nginx/certs/$(DOMAIN).ext

	@echo "✅ SAN certificate created for $(DOMAIN)"


# --------------------------
# WILDCARD CERTIFICATE
# Usage: make wildcard DOMAIN=shop.local
# --------------------------

wildcard:
ifndef DOMAIN
	$(error ❌ DOMAIN is not set! Use: make wildcard DOMAIN=shop.local)
endif

	@echo "==> Creating wildcard certificate for *.$(DOMAIN)"

	mkdir -p nginx/certs

	openssl genrsa -out nginx/certs/wildcard-$(DOMAIN).key 2048

	openssl req -new \
		-key nginx/certs/wildcard-$(DOMAIN).key \
		-out nginx/certs/wildcard-$(DOMAIN).csr \
		-subj "/CN=*.$(DOMAIN)"

	@echo "subjectAltName = DNS:*.$(DOMAIN), DNS:$(DOMAIN)" > nginx/certs/wildcard-$(DOMAIN).ext

	openssl x509 -req \
		-in nginx/certs/wildcard-$(DOMAIN).csr \
		-CA nginx/ca/rootCA.crt \
		-CAkey nginx/ca/rootCA.key \
		-CAcreateserial \
		-out nginx/certs/wildcard-$(DOMAIN).crt \
		-days 365 -sha256 \
		-extfile nginx/certs/wildcard-$(DOMAIN).ext

	@echo "✅ Wildcard certificate created: *.$(DOMAIN)"

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
