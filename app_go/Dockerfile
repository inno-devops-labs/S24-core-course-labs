FROM golang:1.21-alpine as builder

LABEL stage=gobuilder

ARG runcmd=app_go

RUN adduser -D builderuser

RUN apk update --no-cache
RUN apk add gcompat --no-cache
RUN apk add --no-cache tzdata

RUN mkdir -p /app_go/dev && chown -R builderuser /app_go/dev
RUN mkdir -p /app_go/out && chown -R builderuser /app_go/out

USER builderuser

WORKDIR /app_go/dev

COPY go.mod go.sum ./
RUN go mod download
RUN go mod verify

COPY ./cmd ./cmd/
COPY ./internal ./internal/

RUN go build -o /app_go/out/service ./cmd/$runcmd

FROM alpine

LABEL stage=runner

RUN adduser -D appuser
RUN mkdir -p /app && chown -R appuser /app

RUN apk update --no-cache && apk add --no-cache ca-certificates

USER appuser

COPY --from=builder /usr/share/zoneinfo/Europe/Moscow /usr/share/zoneinfo/Europe/Moscow
ENV TZ Europe/Moscow

WORKDIR /app
COPY --chmod=+x --from=builder /app_go/out/service ./service
COPY .env ./
COPY ./templates ./templates/
CMD ./service
