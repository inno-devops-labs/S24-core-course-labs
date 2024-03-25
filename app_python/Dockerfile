FROM python:3.12.0-alpine

WORKDIR /code

RUN apk add --update --no-cache \
    alpine-sdk \
    libffi-dev \
    openssl-dev \
    python3-dev

RUN adduser -D user
RUN chown -R user /code
USER user

RUN python -m pip install poetry==1.7.1

COPY poetry.lock /code
COPY pyproject.toml /code

RUN python -m poetry install

COPY src src
COPY tests tests

CMD ["python", "-m", "poetry", "run", "uvicorn", "src.app:app", "--host", "0.0.0.0"]
