# timur_harin_devops

FROM python:3.11-slim-buster

WORKDIR /app_python

RUN pip install poetry --no-cache-dir

RUN adduser nonroot

USER nonroot

# I have to copy all files from current dir to /app_python, because here a lot of files are needed
COPY --chown=nonroot:nonroot . /app_python

RUN poetry install --no-cache

EXPOSE 5000

CMD ["poetry", "run", "python", "app.py"]

HEALTHCHECK --interval=1m --timeout=3s CMD curl --fail http://localhost:5000/ || exit 1