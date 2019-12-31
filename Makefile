all: install

configure:
	@poetry install

test:
	@poetry run pytest

lint:
	@poetry run flake8

selfcheck:
	@poetry check

check: selfcheck test lint

build: check
	@poetry build

.PHONY: all configure test lint selfcheck check build install
