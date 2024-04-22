# Python Web Application for Displaying Current Time in Moscow

[![CI](https://github.com/hugowea/S24-core-course-labs/actions/workflows/ci.yml/badge.svg)](https://github.com/hugowea/S24-core-course-labs/actions/workflows/ci.yml)

This is a Python-based web application that displays the current time in Moscow.

## Features

- Retrieves the current time in Moscow and displays it on the home page.
- Automatically updates the displayed time every second.

## Installation

1. Make sure you have Python 3.x installed on your system.
2. Clone this repository to your local machine.
3. Navigate to the `k8s/app-python` folder.
4. Create a virtual environment (optional but recommended).
5. Install the required dependencies by running the command: `pip install -r requirements.txt`.

## Docker

### Building the Docker Image

To build the Docker image for this application, execute the following command:

    docker build -t devops-py-app-image .

### Pulling the Docker Image

If you prefer not to build the image locally, you can pull it from Docker Hub. Use the following command:

    docker pull hugowea123/devops-labs-py:correct

### Running the Docker Image

To run the Docker image built locally, use the following command:

    docker run -p 5000:5000 devops-py-app-image

To run the Docker image pulled from public Hub, use the following command:

    docker run -p 5000:5000 hugowea123/devops-labs-py:correct

Once the container is running, you can access the application by opening a web browser and navigating to `http://localhost:5000`.

## Usage

1. Run the application by executing the command: `python app.py`.
2. Open a web browser and visit `http://localhost:5000` to see the current time in Moscow.

## Endpoints

- `/`: Home page that displays the current time in Moscow and increments the visit count.
- `/visits`: Endpoint that displays the recorded visit count.
- `/metrics`: Endpoint to access application metrics in Prometheus format.

## Unit Tests

The application includes comprehensive unit tests to ensure its functionality and quality. These tests cover various aspects of the application, including the routes, rendering, and time updates.

To run the unit tests, execute the following commands:

    pip install -r requirements.txt
    python -m unittest test_app.py

## Contributing

Contributions to enhance the functionality of the application are welcome. To contribute, please follow these steps:

1. Fork the repository and clone it to your local machine.
2. Create a new branch for your feature or bug fix: `git checkout -b feature-name`.
3. Implement your changes and ensure that tests pass.
4. Commit your changes: `git commit -m 'Add feature'`.
5. Push to the branch: `git push origin feature-name`.
6. Open a pull request, describing your changes and any relevant information.

## License

The project is licensed under an [MIT license](LICENSE).
