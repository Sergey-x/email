APPLICATION_NAME = notifier

install:
	poetry install && \
	poetry shell && \
	pre-commit install

run:  ##@Application Run app
	python notifier/main.py

format:
	isort .

lint:
	isort --check . && \
	flake8 . --count --statistics && \
	export MYPYPATH=notifier/ && \
	mypy --namespace-packages notifier/ --explicit-package-bases && \
	export MYPYPATH=

env:
	cp .env.example .env
