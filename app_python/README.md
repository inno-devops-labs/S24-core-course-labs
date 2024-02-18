![workflow](https://github.com/sabonlise/S24-core-course-labs/actions/workflows/main.yaml/badge.svg)

## Overview
Minimalistic Python web application that shows current Moscow time
![](https://i.imgur.com/MLmOJsR.png)
## Installation Instructions

### Installation
1. Clone the source code from this GitHub repository (ensure using the correct branch `lab1`):
    ```sh
    $ git clone -b lab1 https://github.com/sabonlise/S24-core-course-labs
    ```
2. Create new virtual environment:
    ```sh
    $ cd app_python
    $ python -m venv venv
    ```
3. Active the virtual environment:
    ```sh
    $ source venv/bin/activate
    ```
4. Install required Python packages from `requirements.txt`:
   ```sh
   (venv) $ pip install -r requirements.txt
   ```


### Running the Application
Serve the Flask application:
```sh
(venv) $ flask --app app run
```
Navigate to `http://127.0.0.1:5000` in your favorite web browser to access the service


## Testing
You can run the tests with the following command:
```sh
(venv) $ python -m pytest -v
```

## Docker
You can also build this application with Docker
### Building the Image
```sh
$ docker build -t moscow-time-webapp .
```

### Pulling the Image
```sh
$ docker pull soralin/moscow-time-webapp
```

### Running the Image
```sh
$ docker run -d -p 8080:5000 soralin/moscow-time-webapp
```
The app will now be available at `http://localhost:8080`

## CI Workflow
This project uses GitHub Actions for automated building, testing, linting, security vulnerability checking and Docker 
image deployment. It consists of the following steps:
1. Building: python-3.11.2 and all dependencies are installed.
2. Linting: `flake8` is used for Python code linting to detect code-style violations and potential errors.
3. Testing: Unit tests run using the `pytest` framework to ensure code functionality correctness.
4. Security: Vulnerabilities are scanned with the use of `snyk`.
5. Docker deployment: Upon successful completion of previous steps, the image is deployed to the Docker Hub.