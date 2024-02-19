# Date and Time in Moscow

## Table of Content

<!--toc:start-->
- [Date and Time in Moscow](#date-and-time-in-moscow)
  - [Table of Content](#table-of-content)
  - [Overview](#overview)
  - [Running in Docker](#running-in-docker)
  - [Running Locally](#running-locally)
<!--toc:end-->

## Overview

An app that displays Moscow date and time that should be agnostic to the
timezone of the environment it is run on.

Application is written in Scala using ZIO, Tapir and Vert.x, see [SCALA.md](./SCALA.md) for
more details

## Running in Docker

Requirements:

- `Docker`
- `Docker Compose`

You need to simply run

```bash
docker compose up
```

Upon building, it will run tests, and then you will be able to run container.

Application can be accessed on http://localhost:8080/

## Running Locally

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
