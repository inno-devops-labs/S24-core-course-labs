# Time Table Web App

Simple web application written in Go which shows the time in Moscow on each page reload.

## Prerequisites

Before launching application install dependencies with:

```bash
    go install
```

## Starting the app

To start the server, run from `app_go` folder:

```bash
    go run server.go
```

Afterwards, this application will be available on `localhost:8080/`

## Docker

This application can be containerized with docker.

### Build or Pull

You can build a container by running:

```bash
docker build -t <TAG> app_go/
```

Or you can pull existing container from Docker Hub:

```bash
docker pull ramprin/devops_go:latest
```

### Run

In order to run container use the following command:

```bash
docker run -p 80:8080 ramprin/devops_go:latest
```

After this, your application will be available on <http://localhost>

## CI

![example workflow](https://github.com/RamPrin/DevOps-S24/actions/workflows/gotest.yaml/badge.svg)

