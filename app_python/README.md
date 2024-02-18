# DevOps course Labs

![example workflow](https://github.com/github/docs/actions/workflows/python-app.yaml/badge.svg)

## Description

Simple Python web application that shows current time (Moscow timezone).

### Setup

Make sure you have `make` tool on your Unix OS; enter the `app_python` folder and setup enviroment with `make init`. It will create `venv` with all installed needed dependencies. Also it will setup `pre-commit` to check commits (uses `.pre-commit-config.yaml`).

Keep in mind, if you want to act in `venv`, write `source venv/bin/activate` in folder terminal.

### Run

Run web server use `make run` command or `bash start.sh` in `venv` terminal. Web application with formatted Moscow time (and date actually) will be available on `http://0.0.0.0:8000/`. Try to refresh page to update info.

### Tests

To run tests use `make test` or

```
PYTHONPATH=. pytest tests/
```
make sure you have activated virtualenv with `source venv/bin/activate`. `PYTHONPATH` needed to specify certain "root" for correct imports.

### Following code style

Format features (linters + codebase style) can be run via `make format`, and static typecheck with `make typecheck` commands.


## Docker

> Make sure you have installed Docker on your machine, check if docker deamon is running.

To pull image from Docker Hub use make command `make docker-pull` or write in terminal `docker pull adarika/devops-lab-02-python`, to run it use `make docker-pull-run`

To build image from  Dockerfile in directory use make command `make docker-build` or write in terminal `docker build . -t devops-lab-02-python`

To run image builded locally use make command `make docker-run` or write in terminal `docker run -p 8000:8000 --rm -ti devops-lab-02-python`

To push local builded image to Docker Hub use make command `make docker-push`


## CI workflow

### Setup (dependencies), Lint checks, testing code
1. CI starting with setup Python and init venv with dependencies via `make init`, 
2. Then starting to use lnters for checking source code quality
3. After steps above CI run unit tests for checking functional

### Snyk check

In separate job Snyk scanning applies for installed dependencies to ensure all are safe to use

### Building and deploying
1. Logining in DockerHub to be able to push new image in public space afterwards. Login process is using GitHub repository secrets to recieve `DOCKERHUB_USERNAME` and `DOCKERHUB_ACCESS_TOKEN`
2. Then workflow starting to build Docker image, it also push built Docker image to GitHub using username from creds (described above)
3. Build is cahced for optimization of fututre build
