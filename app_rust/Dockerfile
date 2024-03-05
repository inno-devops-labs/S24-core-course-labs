FROM rust:1.75-slim@sha256:70c2a016184099262fd7cee46f3d35fec3568c45c62f87e37f7f665f766b1f74 as builder

WORKDIR /app_data
COPY Cargo.toml Cargo.toml
COPY Rocket.toml Rocket.toml
COPY src/main.rs src/main.rs
RUN cargo build --release

FROM ubuntu:22.04@sha256:e9569c25505f33ff72e88b2990887c9dcf230f23259da296eb814fc2b41af999
EXPOSE 9000
RUN adduser myuser && mkdir /app_data
COPY --chmod=555 --from=builder /app_data/target/release/web-app-framework /app_data/app
COPY --chmod=444 --from=builder /app_data/Rocket.toml /app_data/Rocket.toml
USER myuser
WORKDIR /app_data
ENTRYPOINT ["./app"]
