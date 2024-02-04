# Go Web Application

This is a simple Go web application that displays the current time in Moscow.

# Overview

The application is built using the Fiber framework, providing a lightweight and fast foundation for building web
applications in Go.

The test file with env variables is provided in ```env.test```

The app starts the http server and accept GET requests on ```/```, which returns the `200` status code with json in format
```json
{"time":"2024-02-05T00:47:33+03:00"} 
```
In `RFC3339`

# Installation

1. Clone this repository.
2. Navigate to the app_go folder.
3. Ensure you have `go` with version at least `1.21.5`.
4. Run `go mod tidy` to install dependencies.

# Usage

1. Run the application using `go build -o main cmd/app/* && ./main`.
2. Access the application at http://localhost:8080.

# Tests
1. Run `go test ./... -v`

# Structure

1. `main.go`: Contains the main application logic, including server setup and graceful shutdown handling.
2. `api`: Directory containing HTTP API-related code, including server initialization and request handlers.
3. `service`: Directory containing the clock service implementation.
4. `go.mod`: Specifies the required dependencies.
5. `README.md`: Provides an overview of the application and installation instructions.
6. `GO.md`: Describes best practices, coding standards, and testing approaches applied