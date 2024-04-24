# Bun App

![Bun](https://github.com/pptx704/S24-devops-labs/actions/workflows/build-bun.yaml/badge.svg)

This is a simple web application that displays the current time in Moscow. The application is developed using typescript and Bun is used as the runtime.

![Screenshot](https://i.postimg.cc/XYVk7s95/image.png)

## Table of Contents

- [Bun App](#bun-app)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
    - [Requirements](#requirements)
    - [Installation Steps](#installation-steps)
    - [Docker](#docker)
  - [Development](#development)
    - [Unit Tests](#unit-tests)
    - [CI Workflow](#ci-workflow)

## Installation

### Requirements

- Bun v1.0.0 or higher

### Installation Steps

- Clone this branch to your local machine

```bash
git clone git@github.com:pptx704/S24-devops-labs -b lab1
```

- Navigate to the `app_bun` folder

```bash
cd app_bun
```

- Install the required packages

```bash
bun install
```

- Build the application and run it

```bash
bun build ./entry.ts --outdir ./out
bun run ./out/entry.js
```

The application will be available at [localhost:3000](http://localhost:3000/)

### Docker

It is possible to either build the Docker image from the Dockerfile or pull the image from the Docker Hub.

To build the image, use the following command:

```bash
docker build -t app_bun .
```

To pull the image from the Docker Hub, use the following command:

```bash
docker pull pptx704/app_bun:latest
```

After building or pulling the image, the container can be run with the following command:

```bash
docker run -p 3000:3000 app_bun
```

The application will be available at [localhost:3000](http://localhost:3000/)


In `/` endpoint, it will show the current time in Moscow-

![Screenshot](https://i.postimg.cc/90hqgfp9/image.png)

In `/visits` endpoint, it will show the number of visits to the `/` endpoint.

![Visits](https://i.postimg.cc/JhtdgWYW/image.png)


## Development

Contributions are not accepted at the moment as this is just a lab assignment. You can fork the repository for your own use.

### Unit Tests

Unit tests are maintained in the `test.py` file. To run the tests, use the following command:

```bash
bun test
```

To check the code coverage, use the following command:

```bash
bun test --coverage
```

### CI Workflow

A CI workflow is maintained in the `.github/workflows/build-bun.yaml` file. This workflow lints and tests the application, checks code vulnerability using SNYK, and builds and pushes docker image. Workflow is triggered only if the there is a change in the `app_bun` directory or the workflow file itself.

The CI workflow contains 3 jobs. Each job has a specific set of tasks to perform:

- Build: This job lints and tests the application
- Security: This job checks code vulnerability using SNYK
- Docker: This job builds and pushes the docker image to the Docker Hub. The job is carried out only if the previous jobs are successful.

More details about the CI workflow can be found in the [CI.md](CI.md) file.
