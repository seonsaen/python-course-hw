PYTHON = src/venv/bin/python

MANAGE = src/manage.py

DOCKER_COMPOSE = deploy/docker-compose.yml

run:
	$(PYTHON) $(MANAGE) runserver

migrations:
	$(PYTHON) $(MANAGE) makemigrations

migrate:
	$(PYTHON) $(MANAGE) migrate

superuser:
	$(PYTHON) $(MANAGE) createsuperuser

docker-up:
	docker compose -f $(DOCKER_COMPOSE) up -d

docker-down:
	docker compose -f $(DOCKER_COMPOSE) down

freeze:
	pip freeze > src/requirements.txt