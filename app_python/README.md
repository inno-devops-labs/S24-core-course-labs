# Flask Web Application: Moscow Time Display

This Flask web application displays the current time in Moscow on the main page. The time is updated every time the page is refreshed.

The project was created as the first laboratory work of the Devops course.

## Installation

Follow these steps to set up the project locally:

### Prerequisites

- Python 3.x
- pip package manager

### Installation Steps

1. Clone the repository:

    ```bash
    git clone <repository-url>
    ```

2. Navigate to the project directory:

    ```bash
    cd app_python
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:

    ```bash
    python app.py
    ```

5. Open a web browser and go to `http://127.0.0.1:5000/` to view the application.

### Deployment via docker

1. To build image locally use the following command from app_python dir:

    ```bash
    docker build . --tag app_python
    ```

2. To verify the image is built run:

    ```bash
    docker images
    ```

    You will get something like:
    ```console
    REPOSITORY   TAG       IMAGE ID       CREATED              SIZE
    app_python   latest    87d2f7f96999   About a minute ago   1.03GB
    ```

3. You can also pull the image from dockerhub:

    ```bash
    docker pull happystove/app_python:1.0
    ```

4. To run:
    
    ```bash
    docker run app_python
    ```

    Or if you use dockerhub:

    ```bash
    docker run happystove/app_python:1.0
    ```

## Files Overview

- `app.py`: Contains the Flask application code, including route definitions and the function to retrieve Moscow time.
- `templates/`: Contains html templates.
- `test.py`: Contains unit tests for the Flask application.
- `requirements.txt`: Lists the dependencies required for the project.
- `PYTHON.md`: Describes the reason for choosing the framework, best practices, and implementation details.
- `README.md`: Provides an overview of the project, installation instructions, and file descriptions.

## Usage

Once the Flask application is running locally, open a web browser and navigate to `http://127.0.0.1:5000/` to view the application. The main page will display the current time in Moscow, which will be updated every time the page is refreshed.

## License

[License information, if applicable]


