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

## Docker

> Make sure you have installed Docker on your machine, check if docker deamon is running.

- To pull image from Docker Hub use make command `make docker-pull` or write in terminal `docker pull adarika/devops-lab-02-rust`, to run it use `make docker-pull-run`

- To build image from  Dockerfile in directory use make command `make docker-build` or write in terminal `docker build . -t devops-lab-02-rust`

- To run image builded locally use make command `make docker-run` or write in terminal `docker run -p 8000:8000 --rm -ti devops-lab-02-rust`

- To push local builded image to Docker Hub use make command `make docker-push`

## CI workflow

### Setup (dependencies), Lint checks, testing code
Firstly, setup Rust with `actions-rs/toolchain@v1`, lint with `cargo fmt -- --check` and test with `cargo test` inside steps.

### Snyk check

Unfortunately, there is no snyk for Rust lang, but it is already secure enough by default

### Building and deploying
The same process as for the `app_python`:

1. Logining in DockerHub to be able to push new image in public space afterwards. Login process is using GitHub repository secrets to recieve `DOCKERHUB_USERNAME` and `DOCKERHUB_ACCESS_TOKEN`
2. Then workflow starting to build Docker image, it also push built Docker image to GitHub using username from creds (described above)
3. Build is cahced for optimization of fututre build
