FROM python:3.12-alpine3.18

ENV PYTHONUNBUFFERED 1

WORKDIR /app

# user
RUN addgroup -S group && adduser -S user -G group
USER user

# deps
COPY requirements.txt .
RUN pip install -r requirements.txt

# app
COPY app ./app

EXPOSE 8080

ENTRYPOINT ["python", "app/server.py"]