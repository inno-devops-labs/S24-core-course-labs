[![Python App Pipeline](https://github.com/SokolOFFF/S24-Devops-core-course-labs/actions/workflows/app_python.yaml/badge.svg?event=push)](https://github.com/SokolOFFF/S24-Devops-core-course-labs/actions/workflows/app_python.yaml)

# Moscow time & date displayer 

## Main description 
An application which shows the current time and date in Moscow.

## Running 
To run the app one should proceed the following:
* clone the repo;
* create a virtual environment (as one wishes);
* activate environment;
* run `pip install -r requirements.txt` to install all needed dependencies;
* run `pre-commit install` to install 'pre-commit' to one's venv;
* in folder `app_python` run `python src/app.py`;
* open `http://127.0.0.1:5000/`;
* enjoy.

## Unit Testing
To test the application one should just run `pytest` command in `app_python` folder. By this, all the tests in `tests` folder will be run.

## Docker usage 
### Building on local machine
To build a Docker image do the following:
* change directory to `app_python`;
* build the image as following:<br>
```docker build -t IMAGE_NAME .```<br>
To run on local do the following:<br>
```docker run -dp 8080:8080 --name CONTAINER_NAME IMAGE_NAME```<br>
After this, the app will be available on `http://127.0.0.1:8080/`.

### Using image from Docker Hub
To download and run the image from Docker Hub do the following:
* pull the image (you can ignore `TAG_NAME` if you want to pull the `latest` image):<br>
```docker pull sokolofff/app_python:TAG_NAME```<br>
* run container:<br>
```docker run -dp 8080:8080 --name CONTAINER_NAME sokolofff/app_python:TAG_NAME```<br>
After this, the app will be available on `http://127.0.0.1:8080/`.

## CI workflow
Continuous Integration is hold by `.github/workflows/app_python.yaml` file. The CI has 3 main jobs:
* build - builds project, installs needed requirements by `pip install -r requirements.txt`, linters code with `flake8` and tests with `pytest`;
* security - checks code on vulnerability presents by using SNYK and saves report to `GitHub Code Scanning`;
* docker - builds and pushes image to 'DockerHub' account, triggers only if previous two jobs are successfully done.

The whole workflow triggers only on 'push' changes in 'app_python/' folder or on the workflow file changes.
Best practices used in workflow implementation are described in `CI.md`. 

## Quality checking 
To check the quality of the written code, it is possible to commit changes and run `pre-commit` command. It will show all preferable changes for the whole project. Also, it is possible to use 'flake8' linter in the project.
