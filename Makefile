USER ?= $(shell whoami)
REPO ?= template-ml-service
.PHONY: install run lint type test docker-build
install:
	python -m pip install -U pip && pip install -e .[dev]
run:
	uvicorn src.template_service.app:app --reload --port 8080
lint:
	ruff check .
type:
	mypy src
test:
	pytest -q
docker-build:
	docker build -f docker/Dockerfile -t ghcr.io/${USER}/${REPO}:local .
