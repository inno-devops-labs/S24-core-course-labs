# Go Web App with Random Joke of the Day

## Overview
This is a simple web application that displays a random joke of the day. The application is built using the Go programming language and the Gin web framework.

## Installation and Setup

Run the following commands to install the application:

```bash
# make sure you have Go installed
go version

# make sure you are in the app_go directory
pwd

# install the application
go get .

# run the application
go run main.go
```

Open your browser and navigate to http://localhost:8080/ to see a random joke of the day.

## Docker
This application is also available as a Docker container. To run the application in a Docker container, follow the instructions below.

- **Build locally**
  ```bash
    # Make sure you are in the app_go directory
    pwd

    # Build the Docker image
    docker build --tag abuwho/app_go:latest .

    # Run the Docker container
    docker run -d -p 8080:8080 abuwho/app_go:latest
  ```
  Open your browser and navigate to http://localhost:8080/

Or, 

- Pull from Docker Hub
  ```bash
    # Pull the Docker image
    docker pull abuwho/app_go:latest

    # Run the Docker container
    docker run -d -p 8080:8080 abuwho/app_go:latest
  ```
  Open your browser and navigate to http://localhost:8080/