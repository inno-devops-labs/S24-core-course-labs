FROM python:3.9-slim AS base

RUN adduser appuser

WORKDIR /app

FROM base AS dependencies

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM base AS release

COPY --from=dependencies /usr/local /usr/local

COPY app.py ./
COPY templates ./templates
COPY services ./services

ENV VISIT_COUNTER_PATH='/etc/app_python/tmp/visits.txt'
RUN mkdir -p /etc/app_python/tmp  \
    && chgrp -R appuser /etc/app_python && chmod g+rw -R /etc/app_python

EXPOSE 5000
USER appuser

CMD ["python", "app.py"]
