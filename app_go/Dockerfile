FROM golang:1.17-alpine AS build

WORKDIR /app

COPY go.mod main.go ./

RUN go build -o main

FROM alpine:3.14

WORKDIR /app

COPY --from=build --chmod=0755 /app/main ./main
COPY static ./static

RUN adduser -D user && chown -R user /app

USER user
EXPOSE 8080

ENTRYPOINT ["/app/main"]
