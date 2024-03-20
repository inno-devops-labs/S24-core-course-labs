FROM python:3.12-alpine3.19 as base

LABEL org.opencontainers.image.created="2021-10-10T00:00:00Z" \
    org.opencontainers.image.authors="Fedor Ivanov <ivnfedor@gmail.com>" \
    org.opencontainers.image.url="https://github.com/fedor-ivn/devops/"

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

WORKDIR /app

FROM base as builder

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.7.1

RUN pip install "poetry==$POETRY_VERSION"

COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.in-project true && \
    poetry install --only=main --no-root

FROM base

EXPOSE 80
ENV VIRTUAL_ENV=/app/.venv
ENV PATH="${VIRTUAL_ENV}/bin:$PATH"
ENV USER=uvicorn

RUN apk add --no-cache wget && adduser -D ${USER}

COPY --from=builder /app/.venv ${VIRTUAL_ENV}
COPY main.py main.py

USER ${USER}
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
