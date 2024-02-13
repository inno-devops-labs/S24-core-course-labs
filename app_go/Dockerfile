FROM golang:1.21-alpine AS builder
WORKDIR /app
COPY go.mod go.sum ./
RUN go mod download
COPY ./cmd ./cmd
COPY ./internal ./internal
RUN CGO_ENABLED=0 GOOS=linux go build -o app ./cmd/app


FROM alpine:3.14
ARG USER_NAME=myuser
RUN adduser -D $USER_NAME && \
    mkdir /app && chown -R $USER_NAME /app

RUN apk add --no-cache tzdata

USER $USER_NAME
WORKDIR /app
COPY --from=builder /app/app .
EXPOSE 8080
CMD ["./app"]
