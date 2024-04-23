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

COPY src src
COPY tests tests

RUN mkdir visits_folder

RUN python -m poetry install

CMD ["python", "-m", "poetry", "run", "python", "src/app.py"]
