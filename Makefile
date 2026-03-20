# development commands
dev-compose-up:
	docker compose -f docker-compose.dev.yaml up -d --build

dev-compose-down:
	docker compose -f docker-compose.dev.yaml down -v

dev-compose-logs:
	docker compose -f docker-compose.dev.yaml logs -f

dev-alembic-revision:
	docker compose -f docker-compose.dev.yaml exec bot poetry run alembic revision --autogenerate

dev-alembic-migrate:
	docker compose -f docker-compose.dev.yaml exec bot poetry run alembic upgrade head


# production commands
prod-compose-up:
	docker compose -f docker-compose.prod.yaml up -d

prod-compose-down:
	docker compose -f docker-compose.prod.yaml down

prod-compose-logs:
	docker compose -f docker-compose.prod.yaml logs
