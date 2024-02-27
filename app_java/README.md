# Java Sample Application

![workflow](https://github.com/dmfrpro/s24-core-course-labs/actions/workflows/app_java.yaml/badge.svg)

## Overview

This is a simple java web application that shows current time in **Samara**.

## Installation

- Clone this repository and navigate to the project directory:

```bash
git clone https://github.com/dmfrpro/S24-core-course-labs -b lab1
cd S24-core-course-labs/app_java
```

- Install [maven](https://www.baeldung.com/install-maven-on-windows-linux-mac)

- Run the application and test:

```bash
mvn install
curl localhost:8000
```

## Docker

### Build

```bash
cd S24-core-course-labs/app_java
mvn clean compile assembly:single
docker build --build-arg \
    JAR_FILE=target/app-0.0.1-SNAPSHOT-jar-with-dependencies.jar \
    --tag=dmfrpro/app_java:v1.0 .
```

### Pull and Run

```bash
docker pull dmfrpro/app_java:v1.0
docker run -p 8000:8000 dmfrpro/app_java:v1.0
```

## CI Workflow

### Setup

1. CI starts with linting using `googlejavaformat` linter (`lint` job)
2. Then it installs dependencied and run unit tests via `mvn test` provided by
   `JUnit 5.7` (`test` job)

### SNYK

After two jobs above completed, `snyk_check` job runs

### Building Docker image & Deploying

1. First of all the job starts with logging into Dockerhub using
   `DOCKER_USERNAME` and `DOCKER_TOKEN` repo secrets
2. Then it builds and pushes an image to Dockerhub
3. Build is cached in order to optimize future pipelines
