[![Python application](https://github.com/smasIner/S24-core-course-labs/actions/workflows/main.yaml/badge.svg)](https://github.com/smasIner/S24-core-course-labs/actions/workflows/main.yaml)

# Python Web Application

This is a simple Python web application that displays the current time in the Moscow timezone (MSK). It uses **Flask** as the web framework and **pytz** for timezone handling.

## Installation

Follow the steps below to set up the application locally.

### 1. Clone the repository

First, clone the repository to your local machine.


### 2. Set up a Virtual Environment

To ensure that the application runs in an isolated environment with all the necessary dependencies, create and activate a virtual environment.

**On macOS/Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**

```bash
python -m venv venv
.\venv\Scripts\activate
```

### 3. Install the Dependencies

Once the virtual environment is activated, install the required Python packages using **`pip`**:

```bash
pip install -r requirements.txt
```

### 4. Running the Application

After installing the dependencies, you can run the web application by executing:

```bash
python3 app.py
```

The application will start a local development server. You should be able to open a web browser and navigate to `http://127.0.0.1:8000/` to see the current time in Moscow.

### 5. Testing the Application

You can manually test the application by simply refreshing the page to check that the time displayed is updated.

### 6. Linting the Code

This project uses **flake8** to check the code for style violations based on **PEP 8**.

To run **flake8** on code, simply use the following command:

```bash
flake8 app.py
```

## Dependencies

- Flask: A lightweight WSGI web application framework.
- pytz: A library to handle timezone conversion and daylight saving time.
- flake8: A linting tool to enforce coding standards (PEP 8).

These dependencies are listed in the `requirements.txt` file and can be installed by running:

```bash
pip install -r requirements.txt
```
---

## Dockerizing the Application


### Building the Docker Image

To build the Docker image locally, use the following command. Make sure you are in the app_python directory.

Change smasiner2 to your username:

```bash
docker build -t smasiner2/python_time_app .
```

### Running the Docker Container

After building the Docker image, you can run the container using the following command:

```bash
docker run -p 8080:8000 --rm smasiner2/python_time_app
```

- The `-p 8080:8000` option maps port 8000 from the container to port 8080 on your local machine.
- Once the container is running, you can open a web browser and visit http://localhost:8080

### Pulling and running the Docker Image from Docker Hub

If you want to pull the pre-built Docker image from Docker Hub, use the following command:

```bash
docker pull smasiner2/python_time_app
docker run -p 8080:8000 --rm smasiner2/python_time_app
```
