# Web Application that displays the current Moscow time

## How to run

1. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

2. Run the application:

    ```bash
    python app_python/app.py
    ```

3. Open the web browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to see the current time in
   Moscow.

## How to Test

```bash
pytest app_python/unittests.py
```

## Running the Docker image

1. Pull the Docker image from Docker Hub:

    ```bash
    docker pull sapushha/sapushha_flask_app
    ```

2. Run the Docker container:

    ```bash
    docker run -p 8080:8080 sapushha/sapushha_flask_app
    ```

## Building the Docker Image

1. Change the current directory to `app_python`:

    ```bash
    cd app_python
    ```

2. Build the Docker image:
    ```bash
    docker build -t sapushha_flask_app .
    ```