ckeck:
	@poetry run flake8 pyrofi

install:
	@poetry install

demonstrate:
	@poetry run python -m pyrofi.menu

.PHONY: check install demonstrate
