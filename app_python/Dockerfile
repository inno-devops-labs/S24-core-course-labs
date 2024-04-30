FROM python:3.9-alpine AS base

RUN adduser -D myuser

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

FROM base AS development

COPY app.py app.py
COPY templates templates

FROM development AS release
EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

RUN mkdir -p /etc/app \
    && chmod 777 /etc/app

USER myuser
CMD ["flask", "run"]
