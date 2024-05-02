build:
	docker compose build --no-cache

up:
	docker compose up 

ps:
	docker compose ps

down:
	docker compose down

exec:
	docker exec -it security_microservice bash

logs:
	docker compose logs -f

# DANGEROUS
reset:
	@
	make down
	docker rmi security_microservice 
	docker compose build --no-cache 
	docker compose up

