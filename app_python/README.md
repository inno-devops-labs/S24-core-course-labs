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