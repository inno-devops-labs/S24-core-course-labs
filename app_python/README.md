# Python Flask Web Application - Moscow Time Display

## Overview

This project is built using the Flask framework to display the current time in Moscow. It demonstrates the
implementation of a simple, yet practical, Python web application following best practices.

## Requirements

- Python 3.x
- Flask
- pytz

## Local Installation

### Clone the repository

```bash
git clone https://github.com/VanyaKo/S24-core-course-labs/tree/main
cd app_python
```

### Set up a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

## Docker

### Dockerfile Breakdown

- **Base Image:** It uses `python:3.9.2-slim` as the base image, which is a lightweight version of a Python runtime
  environment.
- **Working Directory:** The working directory inside the container is set to `/app`.
- **Non-root User:** For security reasons, a non-root user named `myuser` is created and used.
- **Copying Files:** Initially, only `requirements.txt` is copied to install dependencies, minimizing rebuild time when
  other files change. After that, the necessary application files (like `app.py` and the `templates` directory) are
  copied
  into the container.
- **Port Exposing:** Port `8000` is exposed, which is the port the Flask app will run on.
- **Environment Variable:** Sets an environment variable `NAME` with a value of `World`, although this variable is not
  used in the provided `app.py`.
- **Command:** The default command runs `app.py` using Python, which starts the Flask application.

### How to Build the Docker Image

#### Prepare your environment

- Ensure Docker is installed and running on your machine.
- Navigate to the root directory of your application (where the `Dockerfile` is located) in a terminal.

#### Build the Docker image

Execute the following command, replacing <image_name> with your desired image name:

```bash
docker build -t <image_name>:latest .
```

This command tells Docker to build an image from the `Dockerfile` in the current directory (`.`), tag it with the name
`<image_name>`, and assign the latest tag.

### How to Pull the Docker Image

If you've pushed your image to a Docker registry (like Docker Hub), you can pull it using:

```bash
docker pull <your_username>/<image_name>:latest
```

Replace `<your_username>` with your Docker Hub username and `<image_name>` with the name of your image. This step is
only necessary if you're pulling an image from a registry, not when you're building it locally.

### How to Run the Docker Container

After building the image, you can run the container with:

```bash=
docker run -d -p 8000:8000 --name <container_name> <image_name>:latest
```

- `-d` runs the container in detached mode (in the background).
- `-p 8000:8000` maps port `8000` of the container to port `8000` on the host, allowing you to access the Flask app via
  `localhost:8000` in your web browser.
- `--name <container_name>` assigns a name to your container for easier reference.
- `<image_name>:latest` specifies which image to use to create the container.
  After running the container, visit [http://localhost:8000] in your browser to see the application displaying Moscow's
  current time.

## Unit Tests

Refer to [Unit Tests Breakdown](PYTHON.md#unit-tests-breakdown) section in `PYTHON.MD`.
