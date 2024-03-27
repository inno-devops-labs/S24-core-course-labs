FROM python:3.11.6-slim

ENV POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_NO_INTERACTION=1
ENV PATH="$POETRY_HOME/bin:$PATH"

WORKDIR /app

RUN pip install --upgrade pip

RUN pip install poetry

COPY pyproject.toml poetry.lock /app/

RUN poetry install

COPY /app /app

EXPOSE 8080

ARG group_name=appgroup
ARG user_name=appuser
RUN groupadd $group_name && useradd -g $group_name $user_name

USER $user_name

ENTRYPOINT ["poetry", "run", "python", "main.py"]

