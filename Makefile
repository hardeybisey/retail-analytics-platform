up:
	@docker compose --profile flower up -d

down:
	@docker compose --profile flower down -v
