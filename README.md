[![Python application](https://github.com/arinazaza/S24-core-course-labs-Zavelevich/actions/workflows/app_python.yml/badge.svg)](https://github.com/arinazaza/S24-core-course-labs-Zavelevich/actions/workflows/app_python.yml)
# Flask Moscow Time Web Application

This is a simple web application built with Flask that displays the current time in Moscow.

## Getting Started

1. Install the required dependencies from the `requirements.txt` file:
   ```shell
   pip install -r requirements.txt
   ```

2. Run the Flask application:
   ```shell
   python app_python.py
   ```

3. Open your web browser and visit `http://localhost:5000` to see the current time in Moscow.

## Docker

### Build

To build the Docker image locally, run the following command in the project's root directory:

```bash
docker build -t image_name .
```

### Pull

To pull the Docker image from a remote repository, use the following command:

```bash
docker arinazaza/app_python.py 
```

### Run

To run the Docker container from the built or pulled image, execute the following command:

```bash
docker run -d --name container_name -p 8000:8000 image_name
```

This command will start a container with the name `container_name`, bind the container's port 8000 to the host's port 8000, and use the `image_name` image.

## Unit tests

This application is covered by unit tests made with Pytest. Tests can be executed by `pytest` command.

## CI workflow 

This repository uses GitHub Actions to automate the linting, testing and building. The workflow is triggered on each push to the `main` branch.

## Dependencies

- Flask
- pytz

## License

[MIT License](LICENSE)