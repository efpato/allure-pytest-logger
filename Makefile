PYTHON ?= python
SRC := allure_pytest_logger tests

build:
	poetry build -n

clean:
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	rm -rf allure-re*
	rm -rf dist

check-isort:
	isort --check-only $(SRC)

check-black:
	black --check $(SRC)

check-pylint:
	pylint $(SRC)

check-mypy:
	mypy $(SRC)

lint: check-isort check-black check-mypy check-pylint

# CODE: FORMAT
isort:
	isort $(SRC)

black:
	black $(SRC)

format: isort black
