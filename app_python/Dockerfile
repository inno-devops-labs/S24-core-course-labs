FROM python:3.12.2-slim-bookworm

WORKDIR /app_python

ENV APP_USER=nonroot

RUN useradd -s /bin/bash -m ${APP_USER} && groupadd docker && usermod -aG docker ${APP_USER}

COPY --chown=$APP_USER:$APP_USER requirements.txt /app_python
RUN pip install --no-cache-dir -r requirements.txt

COPY --chown=$APP_USER:$APP_USER app.py /app_python
COPY --chown=$APP_USER:$APP_USER /templates /app_python/templates

USER ${APP_USER}

EXPOSE 5000

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]