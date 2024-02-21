# Flask Web Application

This is a simple Flask web application that displays the current Moscow time. It provides a basic example of how to create a web application using the Flask framework.

## Features

- Displays the current Moscow time on the homepage.
- Utilizes Flask framework for routing and rendering templates.
- Implements basic error handling for invalid routes.

## Getting Started

To get a local copy of this project up and running, follow these steps:

### Prerequisites

- Python 3 installed on your local machine.
- pip package manager installed.

### Installation

1. Clone the repository to your local machine:

2. Activate venv

3. Install requirements

### Usage

1. Run the Flask application

2. Open a web browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to view the web application.

## Docker

### Building the Docker Image

To build the Docker image locally, follow these steps:

1. Ensure that Docker is installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the root directory of the cloned repository.
4. Run the following command to build the Docker image:
   ```bash
   docker build -t app_python .
   ```

### Pulling the Docker Image

If you prefer to pull the Docker image from Docker Hub instead of building it locally, you can use the following command:

```bash
docker pull almetovkamil/app_python:v1
```

### Running the Docker Container

Once you have the Docker image, you can run the container using the following command:

```bash
docker run -d -p 5000:5000 almetovkamil/app_python:v1
```
This command will run the container in detached mode (`-d`) and map port 5000 on the host to port 5000 in the container.

You can now access your application by navigating to `http://localhost:5000` in your web browser.
