# Go Web App

This Go web application displays the current time in Moscow and dynamically selects a picture based on the time of day.

![example workflow](https://github.com/github/frog-da/DevOps/workflows/go_ci.yml/badge.svg)

## Overview

The project is built with Go (Golang) and utilizes the standard `net/http` package for HTTP handling. It includes a simple web page that showcases the current time in Moscow and dynamically selects a picture corresponding to the time of day (morning, afternoon, or evening).

## Getting Started

Follow these steps to set up and run the Go web app locally:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/frog-da/DevOps/tree/main/app_go
   cd your-repo

2. **Run the Application:**

    ```bash
    go run main.go

3. **Open Your Web Browser:**
    Visit <http://127.0.0.1:8080/view/> to see the web app in action.

## Docker

This application can also be containerized using Docker. Follow the instructions below to build, pull, and run the Docker container.

### How to Build

If you prefer not to build the Docker image locally, you can pull it directly from Docker Hub using:

```bash
docker build -t dianatomiya/devops:g_v1.0 .
```

### How to Pull

If you prefer not to build the Docker image locally, you can pull it directly from Docker Hub using:

```bash
docker run -p 8080:8080 dianatomiya/devops:g_v1.0
```

### How to Run

Once you have the Docker image, you can run the container using:

```bash
docker run -p 8080:8080 dianatomiya/devops:g_v1.0
```

This will run the container, exposing port 8080 on your local machine. You can then access the application in your web browser at <http://localhost:8080/view>.

## CI

This project includes a CI workflow that runs on the `main` branch and pull requests to the `main` branch. The workflow is triggered when changes are made to the `app_go/` directory or the `.github/workflows/go_ci.yml` file. It uses the `ubuntu-latest` environment and has two jobs:

### test

This job sets up the Go environment, lints the code with golangci-lint, runs tests with `go test`, and scans for security vulnerabilities using Snyk. The results are uploaded to GitHub Code Scanning as a SARIF file.

### build-and-publish

This job builds and pushes a Docker image to Docker Hub.

The workflow includes steps to check out the repository, set up Go, run the tests, and perform Docker operations.

Please note that the workflow requires the `SNYK_TOKEN` and `DOCKERHUB_TOKEN` secrets to be set in the repository settings.
