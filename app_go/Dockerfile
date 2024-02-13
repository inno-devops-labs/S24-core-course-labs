FROM golang:1.21 AS builder

RUN useradd --user-group --system --create-home --no-log-init app
USER app
WORKDIR /app
COPY go.mod /app
RUN go mod download
COPY *.go /app
RUN CGO_ENABLED=0 GOOS=linux go build -o app_go

FROM alpine:latest
RUN apk --no-cache add ca-certificates tzdata
COPY --from=builder /app/app_go /app/app_go
COPY view.html /app
WORKDIR /app
EXPOSE 8080
CMD ["./app_go"]
