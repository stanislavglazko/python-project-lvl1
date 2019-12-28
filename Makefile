install:
	poetry install

lint:
	@poetry run flake8 brain_games

check: selfcheck test lint

