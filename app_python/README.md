# Moscow Time Flask Web Application Documentation

## Description

This application is a simple Flask web service that displays the current time in Moscow. It uses the pytz library to
handle timezone conversions and the Flask framework for rendering the webpage.

## Installation

To set up this application, you will need to install the Flask framework and the pytz library. Ensure you have Python
3.9 installed on your machine.

1. Clone the repository

2. Navigate to the project directory:

    ```bash
    cd app_python
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:

    ```bash
    python app.py
    ```

## Usage

Once the app is running, you can access the web service by navigating to <http://localhost:5000/> in your web browser. You
will see the current time in Moscow automatically updating every second.

## Testing

Run the unit tests with the following command:

```bash
python test_app.py
```

## Deployment

For production deployment, set the debug option to False and configure the application to be hosted on a web server such
as Nginx or Apache with a WSGI server like Gunicorn.

```python
if __name__ == '__main__':
    app.run(debug=False, port=8080)
```

Ensure to use environment variables for configuration settings and secrets management in a production environment.

## Using Docker

This application has been Dockerized for easier portability and deployment. Docker packages everything that the application needs to run into a container, making it far simpler to deploy on different systems and platforms.

### Building The Docker Image

You can build the Docker image for this application by using the Docker build command. Make sure to replace <image-name> with the name you want to assign to your Docker image.

```bash
docker build -t <image-name>:<tag> .
```

The -t options sets the name and optionally a tag in the 'name:tag' format. The . signals Docker to use the Dockerfile present in the current directory.

For example, you could build the image as follows:

```bash
docker build -t moscow_time_web_app:1.0 .
```

### Pulling the Docker Image

If the image has been uploaded to a Docker registry, such as Docker Hub, you can pull it using docker pull.

Here're the steps to pull this image from Docker Hub:

```bash
docker pull rmoll/moscow_time_web_app:latest
```

### Running the Docker Container

After building or pulling the Docker image, you can run it with docker run.

To create and start a container, use the following command:

```bash
docker run -d -p 8080:8080 --name moscow_time_container rmoll/moscow_time_web_app:latest
```
This orders Docker to run your image in a new container while also publishing the application's port (8080) to the host.

You should now be able to access the app at http://localhost:8080.

Use docker ps to verify that your container is running, and docker logs <container-id> for inspecting the application logs.
