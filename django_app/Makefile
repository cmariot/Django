DEBUG = 0

BASENAME = app

ifeq ($(DEBUG), 1)
	NAME = $(BASENAME)_dev
	COMPOSE_FILE = docker-compose.dev.yml
else
	NAME = $(BASENAME)_prod
	COMPOSE_FILE = docker-compose.prod.yml
endif


$(NAME): build run

build:
	docker compose -f $(COMPOSE_FILE) build

run:
	docker compose -f $(COMPOSE_FILE) up

stop:
	docker compose -f $(COMPOSE_FILE) down

clean: stop
	docker compose -f $(COMPOSE_FILE) rm -f
	docker compose -f $(COMPOSE_FILE) down --volumes --remove-orphans

fclean: clean
	docker compose -f $(COMPOSE_FILE) down --rmi all

re: fclean build run

list:
	docker compose -f $(COMPOSE_FILE) ps
	docker compose -f $(COMPOSE_FILE) images

.PHONY: build run stop clean
