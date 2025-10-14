install:
\tpip install -U pip && pip install -e .[dev]
run:
\tuvicorn src.<pkg_name>.app:app --reload --port 8080
lint:
\truff check .
type:
\tmypy src
test:
\tpytest -q
docker-build:
\tdocker build -f docker/Dockerfile -t ghcr.io/$(USER)/$(REPO):local .
