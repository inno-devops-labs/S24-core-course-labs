## Description

Simple Rust web application that shows current requests number (and updates on refreshing).

### Setup

Make sure you have `make` tool on your Unix OS; enter the `app_rust` folder.

Also make sure you have `rustc` ([installation guide](https://doc.rust-lang.org/book/ch01-01-installation.html)) + make sure `cargo` tool has installed too.

Aware that `make <command>` is available only from `app_rust/` folder.

### Run

Run web server use `make run` command or `bash start.sh` in terminal. Web application with requests counter will be available on `http://0.0.0.0:8000/`. Try to refresh page to update info.

Of course, you can use `cargo run` but only from `app_rust/app/`.

### Tests

To run tests use `make test` or you can use `cargo test` from `app_rust/app/` folder.