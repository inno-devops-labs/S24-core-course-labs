FROM golang:1.21-alpine3.19 AS build

WORKDIR /app

RUN adduser -h /app -D app && chown -R app:app /app

COPY go.mod /app
COPY main.go /app

RUN go build -o app_go .

FROM alpine:3.19 as final

WORKDIR /app

RUN adduser -h /app -D app && chown -R app:app /app

COPY --from=build /app/app_go .

EXPOSE 8000

USER app

CMD ["./app_go"]
