# Python App

This is a simple web application that displays the current time in Moscow. The application is developed using Python and Flask framework.

## Table of Contents

- [Python App](#python-app)
  - [Table of Contents](#table-of-contents)
  - [Installation](#installation)
    - [Requirements](#requirements)
    - [Installation Steps](#installation-steps)
  - [Development](#development)
    - [Notes](#notes)

## Installation

### Requirements

- Python 3.8 or higher
- `pip` package manager

### Installation Steps

- Clone this branch to your local machine

```bash
git clone git@github.com:Wesam-Naseer/S24-core-course-labs -b lab1
```

- Navigate to the `app_python` folder

```bash
cd app_python
```

- Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

- Install the required packages

```bash
pip install -r requirements.txt
```

- Run the application

```bash
flask run
```

The application will be available at [localhost:5000](http://localhost:5000/)

### Docker

#### Containerized Application

The application is containerized using Docker, ensuring portability and ease of deployment across different environments. Below are instructions for building, pulling, and running the Docker container.

#### How to Build

To build the Docker image locally, follow these steps:

```bash
docker build -t mtz .
```

This command builds the Docker image based on the provided Dockerfile (`Dockerfile`) in the `app_python` directory and tags it with the name `mtz`.

#### How to Pull

If you prefer to pull the pre-built Docker image from a container registry instead of building it locally, you can use the following command:

```bash
docker pull wesamnaseer/mtz:v1.0
```

#### How to Run

Once you have either built the Docker image locally or pulled it from a registry, you can run the container using the following command:

```bash
docker run -p 5000:5000 wesamnaseer/mtz:v1.0
```

## Docker compose

### Run the image

To run the application run:

```properties
docker compose up
```

> Do not forget to give proper permission to visits.txt

### Unit Tests

#### Testing Current Time Formatting

- We have a unit test named `test_current_time_format` which verifies that the current time retrieved by our application is correctly formatted in the expected format (`YYYY-MM-DD HH:MM:SS`).

#### Running the Unit Tests

To run the unit tests for the Python web application, follow these steps:

1. **Navigate to the Application Directory:**

   - Open a terminal or command prompt.
   - Navigate to the directory where your Python web application (`app_python`) is located.

2. **Activate Virtual Environment (if applicable):**

   - If you are using a virtual environment, activate it using the appropriate command for your operating system.

3. **Install Testing Dependencies (if not already installed):**

   - Ensure that the required testing dependencies are installed. You can install them using pip:

     ```
     pip install pytest
     ```

4. **Run the Unit Tests:**

   - Run the following command to execute the unit tests:

     ```
     pytest
     ```

   - This command will discover and run all test cases within the `tests` directory.

5. **View Test Results:**

   - After running the tests, pytest will display the test results in the terminal. You should see information about the test cases executed and whether they passed or failed.
