FROM rust:1.76-alpine3.19 as builder

WORKDIR /build
COPY . .
RUN apk update && apk add --no-cache \
    musl-dev=1.2.4_git20230717-r4 \
    && cargo build --release

FROM alpine:3.19.1

LABEL org.opencontainers.image.created="2021-10-10T00:00:00Z" \
    org.opencontainers.image.authors="Fedor Ivanov <ivnfedor@gmail.com>" \
    org.opencontainers.image.url="https://github.com/fedor-ivn/devops/"

WORKDIR /app

ENV USER=rust
RUN apk add --no-cache wget && adduser -D ${USER}
EXPOSE 80
COPY --from=builder /build/target/release/app_rust ./

USER ${USER}
CMD ["./app_rust"]
