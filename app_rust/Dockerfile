FROM lukemathwalker/cargo-chef:latest-rust-1.72.0 as chef
WORKDIR /app
RUN apt update && apt install lld clang -y

LABEL description="A rust backend for helping students efficiently study their materials" maintainer="ejedavid"

FROM chef as planner
COPY src ./src
COPY Cargo.lock ./
COPY Cargo.toml ./
COPY sqlx-data.json ./
COPY .sqlx ./

# Compute a lock-like file for our project
RUN cargo chef prepare  --recipe-path recipe.json

FROM chef as builder
COPY --from=planner /app/recipe.json recipe.json
# Build our project dependencies, not our application!
RUN cargo chef cook --release --recipe-path recipe.json

COPY --from=planner /app/src ./src
COPY --from=planner /app/Cargo.lock ./
COPY --from=planner /app/Cargo.toml ./
COPY --from=planner /app/sqlx-data.json ./
ENV SQLX_OFFLINE true
# Build our project
RUN cargo build --release --bin learning-rust

FROM debian:bookworm-slim AS runtime
WORKDIR /app

RUN apt-get update -y \
    && apt-get install -y --no-install-recommends openssl ca-certificates \
    # Clean up
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

RUN adduser --disabled-password --gecos '' myuser
RUN mkdir -p /app && chown -R myuser:myuser /app

COPY --from=builder /app/target/release/learning-rust learning-rust
COPY configuration configuration
ENV APP_ENVIRONMENT production
EXPOSE 8001
ENTRYPOINT ["./learning-rust"]