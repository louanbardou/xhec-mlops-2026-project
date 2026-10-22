.PHONY: install lint train prefect-server deploy api docker-build docker-run static

install:
	uv sync
	uv run pre-commit install

lint:
	uv run ruff check . --fix
	uv run ruff format .

train:
	uv run python -m src.modelling.main data/abalone.csv

prefect-server:
	uv run prefect server start

deploy:
	uv run python -m src.modelling.deploy

api:
	uv run uvicorn src.web_service.main:app --port 8001

docker-build:
	docker build -f Dockerfile.app -t abalone-app .

docker-run:
	docker run -p 0.0.0.0:8000:8001 -p 0.0.0.0:4200:4201 abalone-app

static:
	uv run python bin/build_static.py
