FROM python:3.9.18-alpine3.19@sha256:7e53de21917d6793787bc67483838360404bb2fd70d9c3e38ccc243790c323b2

WORKDIR /env

RUN pip install --no-cache-dir poetry==1.7.1

COPY poetry.lock pyproject.toml /env/

RUN poetry config virtualenvs.create false && poetry install

WORKDIR /code

COPY ./app /code/app

ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

EXPOSE 8080
