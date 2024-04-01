up-backend:
	docker compose -f docker-compose.yaml up --build
down-backend:
	docker compose -f docker-compose.yaml down -v
exec-backend:
	docker compose -f docker-compose.yaml exec backend bash
up-all:
	mock
down-all:
	mock