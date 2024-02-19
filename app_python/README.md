# Python Web Application

This is a Python web application built using the Flask framework to display the current time in Moscow.

## Usage

1. Clone the repository:

    ```bash
    git clone <repository_url>
    ```

2. Navigate to the project directory:

    ```bash
    cd project_folder
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:

    ```bash
    python3 app.py
    ```

5. Access the application in your web browser at `http://127.0.0.1:5000/`.

## Docker
Building the Docker Image
 ```bash
    docker build -t <image name> .
```
Pulling the docker Image
 ```bash
    docker pull djhovi/my-flask-app:latest

```
Running the docker Image
 ```bash
    docker run -p5000:5000 djhovi/my-flask-app:latest

```

## Unit Tests

Comprehensive unit tests have been implemented to ensure the reliability and functionality of the Flask web application. These tests cover critical parts of the application and validate its behavior under various conditions.

To run the unit tests, execute the following command in your terminal(in root project folder):

```bash
python3 -m unittest discover -s app_python/src/tests -p "test_application.py"