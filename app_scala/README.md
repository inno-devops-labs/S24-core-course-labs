# Scala Web Application

## Overview

This Scala web application calculates and displays factorials using the Play Framework. It's built adhering to best practices for maintainability, testing, and performance.

## Getting Started

### Prerequisites

- Java JDK 8 or higher
- sbt (Scala Build Tool)

### Running the Application

Start the application using sbt:

```bash
sbt run
```

The application will be accessible at `http://localhost:9000`

### Testing

Execute the tests with:

```bash
sbt test
```

## Building docker image

To build docker image, execute the following commang:

```bash
docker build . -t catdog905/dev-ops-course-app-scala
```

or you can pull the image from Docker Hub

```bash
docker pull docker push catdog905/dev-ops-course-app-scala:latest
```

Currently available versions are latest, 0.1.0

Run docker container from image using

```bash
docker run -p 9000:9000 -e SECRET_KEY="QCY?tAnfk?aZ?iwrNwnxIlR6CTf:G3gf:90Latabg@5241AB`R5W:1uDFN];Ik@n" catdog905/dev-ops-cours-app-scala
```

## Continious integration

There are two workflows in the `.github/workflows/`: `scala.yml` and `docker-publish-scala.yml`

- `scala.yml` is responsible for linters check, unit tests check and snyk security check
- `docker-publish-scala.yml` is responsible for building docker image and publilshing it to docker hub
