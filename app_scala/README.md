[![Scala App Workflow](https://github.com/Skril3366/S24-core-course-labs/actions/workflows/scala.yml/badge.svg)](https://github.com/Skril3366/S24-core-course-labs/actions/workflows/scala.yml)

# Date and Time in Moscow

## Table of Content

<!--toc:start-->
- [Date and Time in Moscow](#date-and-time-in-moscow)
  - [Table of Content](#table-of-content)
  - [Overview](#overview)
  - [Running](#running)
    - [Using Docker](#using-docker)
    - [Using Docker](#using-docker)
    - [Using Docker Compose](#using-docker-compose)
    - [Locally](#locally)
  - [CI workflow](#ci-workflow)
    - [Checks Job](#checks-job)
    - [Build Job](#build-job)
<!--toc:end-->

## Overview

An app that displays Moscow date and time that should be agnostic to the
timezone of the environment it is run on.

Application is written in Scala using ZIO, Tapir and Vert.x, see [SCALA.md](./SCALA.md) for
more details

## Running

### Using Docker

### Using Docker

You may use already built image:

```sh
docker pull skril/moscow-time:scala
docker run -p 8080:8080 skril/moscow-time:scala
```

Or build it yourself:

```sh
docker build -t moscow-time .
docker run -p 8080:8080 moscow-time
```

Now an app can be accessed at http://localhost:8080

### Using Docker Compose

The simplest way to run the app is to:

```sh
docker compose up
```

### Locally

Requirements:

- `Scala 3.3.1`
- `SBT 1.9.8`
- `OpenJDK 17.0.10`

The easiest way to set it all up is to use [SDKMAN](https://sdkman.io/)

Then simply execute to run application

```bash
sbt run
```

And to test application:

```bash
sbt test
```

Note that you can use repl mode of SBT instead:

1. Enter repl mode

```bash
sbt
```

2. Then you can run

```bash
run
```

3. And test

```bash
test
```

It can be accessed on http://localhost:8080/

## CI workflow

This GitHub Actions workflow automates testing and building of your Python
application. It's triggered whenever code changes in `app_python` directory are
pushed.

### Checks Job

The **Checks** job ensures the project passes basic quality checks on every commit by running tests and linting:

1. Clones the repository using the latest Ubuntu environment.
2. Installs OpenJDK 17
3. Uses sbt build tool to manage dependencies
4. Installs all required packages from build.sbt file
5. Performs static analysis using scalafix and scalafmt
6. Executes unit tests using ZIO Test framework

### Build Job

After successful checks, the **Build** job builds and pushes a Docker image to Docker Hub:

1. Sets up Docker Buildx for multi-architecture support.
2. Logins into Docker Hub using secure credentials stored as secrets.
3. Builds and pushes an optimized Docker image based on the provided `Dockerfile`. The tag will be set to `skril/moscow-time:scala`.
