FROM golang:1.21-alpine as builder

RUN adduser -D user
USER user

WORKDIR /app_golang

COPY go.mod ./

RUN go mod download

COPY main.go .

RUN go build -o main .

FROM alpine:3.15

RUN apk --no-cache add tzdata

WORKDIR /app_golang

COPY --from=builder /app_golang/main .

EXPOSE 8080

CMD ["./main"]
