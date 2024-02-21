# Python Web Application

[![Python App](https://github.com/g-akleh/S24-core-course-labs/actions/workflows/python.yaml/badge.svg)](https://github.com/g-akleh/S24-core-course-labs/actions/workflows/python.yaml)

This Python web application displays the current time in Moscow.

## Installation

1. Clone this repository to your local machine:

2. Navigate to the `app_python` directory:

   ```bash
   cd app_python
   ```

3. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Application

1. Ensure you are in the `app_python` directory.

2. Run the application using the following command:

   ```bash
   python app.py
   ```

   Or:

   ```bash
   python3 app.py
   ```

3. Open a web browser and navigate to `http://127.0.0.1:5000/` to view the current time in Moscow.

4. Upon finishing, deactivate the virtual environment:
   ```
   deactivate
   ```

### Running the Unit Tests

1. Ensure you are in the `app_python` directory.

2. Run the test suite using the following command:

   ```bash
   python -m unittest test_app.py
   ```

3. After running the command, you should see the output of the test results.

## Docker

To run the application in a Docker container, follow these steps:

### Building the Docker Image

1. Navigate to the `app_python` directory.

2. Run the following command:

```bash
docker build -t python-web-app .
```

### Running the Docker Container
To run the build image, execute the command:
```bash
docker run -p 5000:5000 python-web-app
```
### Pulling and running the Docker Image

1. Pulling the image from Docker Hub:

```bash
docker pull ghadeero/python-web-app
```

2. Running the pulled image

```bash
docker run -p 5000:5000 ghadeero/python-web-app
```


## Continuous Integration (CI)
This project is integrated with GitHub Actions for continuous integration. The CI workflow includes steps to:
- Install dependencies
- Lint the code using flake8
- Run unit tests
- Utilizing Snyk to check for vulnerabilities
- Login to DockerHub
- Build and push a Docker image

## Technologies Used

- Python
- Flask
- pytz
- Docker

## License
This project is licensed under the MIT License