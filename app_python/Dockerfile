FROM python:3.11-alpine as base

LABEL com.example.version="0.0.1"
LABEL org.opencontainers.image.source="https://github.com/RamPrin/DevOps-S24"

COPY . /server

WORKDIR /server

RUN addgroup server && adduser -D -g server ramprin 

USER ramprin:server

ENV PATH="$PATH:/home/ramprin/.local/bin"

RUN pip install -r requirements.txt

ENTRYPOINT [ "uvicorn", "--host", "0.0.0.0", "--port", "8080", "server:server"]

EXPOSE 8080
