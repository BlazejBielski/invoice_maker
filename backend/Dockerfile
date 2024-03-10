FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

ENV POETRY_VERSION=1.7.1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_HOME='/usr/local'

COPY ./install-poetry.py ./
RUN python3 install-poetry.py --version 1.7.1 \
    && $POETRY_HOME/bin/poetry --version

WORKDIR /app

COPY ./pyproject.toml ./poetry.lock ./

RUN poetry install --no-interaction --no-ansi --no-root

RUN apt-get update && apt-get install -y netcat

COPY ./entrypoint.sh ./

ENTRYPOINT ["./entrypoint.sh"]

COPY . .

RUN poetry install --without dev --sync