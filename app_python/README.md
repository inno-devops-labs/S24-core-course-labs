# Python Web Application

## Overview

This web application displays the current time in Moscow.

## Installation

### GitHub Repository

The installation requires at least Python 3.8 with pip package installer.

1. Download the source code manually or with `git clone`:

    ```bash
    git clone https://github.com/MrFired/S24-core-course-labs.git 
    ```

2. Open `app_python` folder
3. Install required dependencies with pip:

   ```bash
   pip install -r requirements.txt  
   ```

After successful installation, you can run the program from `app_python` folder via

```bash
flask run
```

### Docker

1. Install [Docker](https://docs.docker.com/get-docker/)
2. Pull the image from Docker Hub repository:

   ```bash
   docker pull mrfired/devops-course:lab2
   ```

You can run the application in the container with

```bash
docker run -p 5000:5000 mrfired/devops-course:lab2
```

Then you will be able to use the application on `localhost:5000`

## Unit Tests

To test the application after installation simply run from within virtual environment:

```bash
pytest
```

> Note: Testing is not available in Docker installation.

## CI Workflow

The Continuous Integration workflow for the project consists of the following steps:

1. **Set up**: configuring the environment for CI;
2. **Dependencies**: installing requirements;
3. **Lint**: linting the project sources;
4. **Test**: testing the implementation;
5. **Docker Build & Push**: building and pushing the image to Docker Hub.
