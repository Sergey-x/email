ARG PYTHON_VERSION=3.10
FROM python:${PYTHON_VERSION}-slim

RUN pip install --upgrade --no-cache pip
RUN pip install poetry

WORKDIR /notifier

COPY ./pyproject.toml .
COPY ./poetry.lock .

RUN poetry export -f requirements.txt --output ./requirements.txt --without-hashes
RUN pip install --no-cache -r ./requirements.txt

COPY . .

ENTRYPOINT python notifier/main.py
