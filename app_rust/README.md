# Simple Web Application

This application is a minimalistic web service built with Rust that provides the
current time in Moscow.

## Prerequisites

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Ensure you have [Rust][rust] and [Cargo][cargo] installed.

[rust]: https://www.rust-lang.org/tools/install
[cargo]: https://doc.rust-lang.org/cargo/getting-started/installation.html

## Running in Docker

To run the application in a Docker container, use the following commands:

```bash
docker pull fedorivn/simple-web-app:rust-1.0.0
docker run --name app -d -p 8000:80 fedorivn/simple-web-app:rust-1.0.0
```

## Running Locally

Start the application using the following command:

```bash
cargo run
```

You can now access the service by visiting `http://127.0.0.1:8001` in your web
browser or using a tool like curl. For example:

```bash
$ curl http://127.0.0.1:8001
{"current_time":"2024-01-31 14:16:05"}
```

## Building the Docker Image

To build the Docker image, use the following command:

```bash
docker build -t simple-web-app:rust .
```

## Testing

This project uses Rust's built-in testing framework. To run the tests, use the
following command:

```bash
cargo test
```

This command will run all the tests in the project and display the results in
the terminal.

## Continuous Integration (CI)

The project uses a robust Continuous Integration:

1. Linting with `cargo fmt` & `cargo clippy`
2. Build & Testing with `cargo test`
3. Push to Docker Hub

The CI process is automated using GitHub Actions and leverages the best
practices described in [Best Practices][ci].

[ci]: ../app_python/CI.md
