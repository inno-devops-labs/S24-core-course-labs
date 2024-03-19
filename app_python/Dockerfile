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

EXPOSE 5000
USER appuser

CMD ["python", "app.py"]
