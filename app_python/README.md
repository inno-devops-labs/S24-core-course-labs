# Python Web Application for Moscow time display

## Set Up

1. (Optional) Create a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install the required dependencies:

   ```bash
    pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python src/app.py
   ```

4. Open your web browser and navigate to `http://
localhost:5000/` to view the application.

5. (Optional) Run the tests:

   ```bash
   python tests/app_test.py
   ```

## Docker

1. To build the Docker image run the following command in the terminal from the `app_python` directory with Dockerfile present:

   ```bash
   docker build -t my-flask-app .
   ```

2. To run the Docker image:

   ```bash
   docker run -p 5000:5000 my-flask-app
   ```

3. Alternatively, you can pull the Docker image from my [dockerhub repository](https://hub.docker.com/repository/docker/ozurexus/my-flask-app) using the following commands:

   ```bash
   docker login
   docker pull ozurexus/my-flask-app
   docker run -p 5000:5000 ozurexus/my-flask-app
   ```

## Stack

- Python
- Flask
- HTML
