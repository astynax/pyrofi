check:
	poetry run flake8 pyrofi
	poetry run mypy pyrofi

install:
	poetry install

demonstrate:
	@poetry run python -m pyrofi

.PHONY: check install demonstrate
