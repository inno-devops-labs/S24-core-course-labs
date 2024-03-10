# Simple Web Application

This application is a minimalistic web service built with Rust that provides the
current time in Moscow.

## Prerequisites

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Ensure you have [Rust][rust] and [Cargo][cargo] installed.

[rust]: https://www.rust-lang.org/tools/install
[cargo]: https://doc.rust-lang.org/cargo/getting-started/installation.html

## Running the Application

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

## Testing

This project uses Rust's built-in testing framework. To run the tests, use the
following command:

```bash
cargo test
```

This command will run all the tests in the project and display the results in
the terminal.
