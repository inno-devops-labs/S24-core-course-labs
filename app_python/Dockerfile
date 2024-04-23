# syntax=docker/dockerfile:1

# Stage 1: Build stage
FROM python:3.12.2-slim-bullseye as builder

LABEL maintainer="almetov.kamil@gmail.com"

WORKDIR /app_python

# Copy requirements.txt to the container
COPY ./app_python/requirements.txt .
RUN pip install --upgrade pip \
    pip install --no-cache-dir -r requirements.txt

# Copy the application source code
COPY ./app_python/ .

RUN chown -R nobody /app_python
RUN chmod a+w /app_python/visits

EXPOSE 5000

USER nobody

# CMD [ "python3", "-m" , "flask", "run"]
ENTRYPOINT ["python3", "app.py"]