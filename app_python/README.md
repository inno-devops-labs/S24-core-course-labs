# Project Overview

This project is a FastAPI-based web application designed to display the current time in Moscow.

## Local Installation

Follow these steps to set up the project locally:

1. Clone the repository:

   ```bash
   git clone https://github.com/frog-da/DevOps/tree/main/app_python
   cd your-repo

2. Install dependencies:

   ```bash
   pip install -r requirements.txt

3. Run the FastAPI application:

    ```bash
    uvicorn main:app --reload

4. Open your web browser and go to <http://127.0.0.1:8000/> to see the current time in Moscow.

Please make sure to update tests as appropriate.

To run the tests:

```bash
pytest
```

## Docker

This application can also be containerized using Docker. Follow the instructions below to build, pull, and run the Docker container.

### How to build

To build the Docker image locally, navigate to the project directory and run:

```bash
docker build -t dianatomiya/devops:p_v1.0 .
```

### How to pull

You can also pull the Docker image directly from Docker Hub using:

```bash
docker pull dianatomiya/devops:p_v1.0
```

### How to run

Once you have the Docker image, you can run the container using:

```bash
docker run -p 80:80 dianatomiya/devops:p_v1.0
```

This will run the container, exposing port 80 on your local machine. You can then access the application in your web browser at <http://localhost>.
