# Moscow Time App

This application provides a straightforward web interface to display the current time in the MSK (Moscow Standard Time) timezone. It's a minimalistic project that demonstrates handling time zones and web responses in Go.

## Technologies Used

- **Programming Language**: Go (GoLang)

## Getting Started

To run the Moscow Time app, you'll need to have Go installed on your system. This application does not rely on any external dependencies, making it simple to set up and run.

### Prerequisites

Ensure you have Go installed on your computer. You can download it from [the official Go website](https://golang.org/dl/).

### Running the Application

Follow these steps to get the application up and running:

1. **Download Dependencies** (Optional):
   Since the application only uses the Go standard library, explicitly downloading dependencies is not required. However, if you've introduced any external packages, you can download them using:
   ```bash
   go mod download
   ```
2. **Start the Server**:
   Launch the application to start the web server. Navigate to the project directory in your terminal and run:
   ```bash
   go run main.go
   ```
   After the server starts, you can view the Moscow Time by visiting [http://localhost:8080/](http://localhost:8080/) in your web browser.

## How to Test

The application comes with a basic testing setup to verify the functionality of the time display. To run the tests, execute the following command in the root directory of the project:

```bash
go test
```

This command will run all tests included in the project, outputting the results to your terminal. Ensure you're in the project's root directory to successfully execute the tests.

## Docker Usage

This section covers building, pulling, and running the Docker container for the application.

### Building the Docker Image

To build the Docker image, run the following command in the project app_golang folder:

```bash
docker build -t xdrdvd/app_golang:latest .
```

### Pushing the Docker Image

To push the Docker image to Docker Hub, run the following command in the project app_golang folder:

```bash
docker push xdrdvd/app_golang:latest
```

### Pulling and running the Docker Container

To pull and run the Docker container, run the following commands:

```bash
docker pull xdrdvd/app_golang:latest
docker run -p 8080:8080 xdrdvd/app_golang:latest
```
