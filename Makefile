up:
	@{ docker-compose up; }

build:
	@{ docker-compose build; }

migrate:
	docker-compose run app db migrate -m '$(message)'

upgrade:
	@{ docker-compose run app db upgrade; }

downgrade:
	@{ docker-compose run app db downgrade; }

format:
	black app
	isort app

check:
	flake8

test:
	@{ \
		docker compose -f docker-compose-ci.yaml up --build -d; \
        docker compose -f docker-compose-ci.yaml run --rm app-test sh -c 'pytest tests/'; \
		docker compose -f docker-compose-ci.yaml down --remove-orphans; \
	}
.PHONY: up auth build migrate upgrade downgrade test test-migration coverage shell format check clear-empty-folders create-network
