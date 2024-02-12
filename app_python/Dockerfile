FROM python:3.11-alpine3.18 AS base

WORKDIR /app

RUN adduser -h /app -D fastapi && chown -R fastapi:fastapi /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py ./

EXPOSE 8000
USER fastapi
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
