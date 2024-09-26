up:
	@{ docker-compose up; }

build:
	@{ docker-compose build; }

migrate:
	docker-compose run app db migrate -m '$(message)'

upgrade:
	@{ docker-compose run app db upgrade; }

format:
	black app tests
	isort app tests

check:
	flake8

.PHONY: up auth build migrate upgrade downgrade test test-migration coverage shell format check clear-empty-folders create-network
