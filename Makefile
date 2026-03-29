# development commands
dev-compose-up:
	docker compose -f docker-compose.dev.yaml up -d --build

dev-compose-down:
	docker compose -f docker-compose.dev.yaml down -v

dev-compose-logs:
	docker compose -f docker-compose.dev.yaml logs -f

dev-alembic-revision:
	docker compose -f docker-compose.dev.yaml exec renthousebot poetry run alembic revision --autogenerate

dev-alembic-migrate:
	docker compose -f docker-compose.dev.yaml exec renthousebot poetry run alembic upgrade head

dev-locale-extract:
	docker compose -f docker-compose.dev.yaml exec renthousebot poetry run pybabel extract -k _:1,1t -k _:1,2 -k __ --input-dirs=src -o locales/messages.pot

dev-locale-init:
	docker compose -f docker-compose.dev.yaml exec renthousebot poetry run pybabel init -i locales/messages.pot -d locales -D messages -l en
	docker compose -f docker-compose.dev.yaml exec renthousebot poetry run pybabel init -i locales/messages.pot -d locales -D messages -l ru
	docker compose -f docker-compose.dev.yaml exec renthousebot poetry run pybabel init -i locales/messages.pot -d locales -D messages -l uz

dev-locale-update:
	docker compose -f docker-compose.dev.yaml exec renthousebot poetry run pybabel update --no-fuzzy-matching -d locales -D messages -i locales/messages.pot

dev-locale-compile:
	docker compose -f docker-compose.dev.yaml exec renthousebot poetry run pybabel compile -d locales -D messages

# production commands
prod-compose-pull:
	docker compose -f docker-compose.prod.yaml pull

prod-compose-up:
	docker compose -f docker-compose.prod.yaml up -d --remove-orphans

prod-compose-down:
	docker compose -f docker-compose.prod.yaml down

prod-compose-logs:
	docker compose -f docker-compose.prod.yaml logs -f
