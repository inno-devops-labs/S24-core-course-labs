FROM rust:1.76-slim AS builder

COPY ./app ./app
WORKDIR /app
RUN cargo build --release

FROM debian:bookworm-slim

WORKDIR /app

RUN adduser --disabled-password app 
COPY --from=builder /app/target/release/app ./
RUN mkdir /app/app_data
RUN chown -R app /app

USER app
EXPOSE 8000

ENTRYPOINT ["./app"]