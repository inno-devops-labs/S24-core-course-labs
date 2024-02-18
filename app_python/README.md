# My Python Web Application

## Description
This Python web application displays the current time in Moscow using the Flask framework.

## Features
- Displays the current time in Moscow.
- Automatically updates the displayed time upon page refreshing.

## Installation
1. Clone the repository to your local machine:
   git clone https://github.com/inga-zimnya/S24-core-course-labs
   cd app_python
2. Install the required dependencies:
   pip install flask
   pip install pytz
3. Install the required packages
   ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Run the application:
     ```bash
    python app_python/app.py
    ```
2. Open your web browser and navigate to http://127.0.0.1:5000/ to view the current time in Moscow.

## Using Docker

1. Pull the Docker image from Docker Hub:

    ```bash
    docker pull i.ezhova/devops-flask-app
    ```

2. Run the Docker container:

    ```bash
    docker run -p 8080:8080 i.ezhova/devops-flask-app
    ```

3. Open the web browser and navigate to [http://127.0.0.1:8080/](http://127.0.0.1:8080/) to see the current time in
   Moscow.

### Building the Docker Image

1. Change the current directory to `app_python`:

    ```bash
    cd app_python
    ```

2. Build the Docker image:
    ```bash
    docker build -t devops-flask-app .
    ```

## Author
Inga Ezhova

## Contact
i.ezhova@innopolis.university