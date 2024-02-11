FROM golang:1.21-alpine as base

LABEL com.example.version="0.0.1"
LABEL org.opencontainers.image.source="https://github.com/RamPrin/DevOps-S24"

COPY . /server

WORKDIR /server

RUN addgroup server && adduser -D -g server ramprin 

USER ramprin:server

RUN go install

ENV PORT=8080

ENTRYPOINT [ "go", "run", "server.go"]

EXPOSE 8080
