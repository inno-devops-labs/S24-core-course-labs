# Go Web App

This Go web application displays the current time in Moscow and dynamically selects a picture based on the time of day.

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
