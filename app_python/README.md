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

## Testing
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

## Quality checking 
To check the quality of the written code, it is possible to commit changes and run `pre-commit` command. It will show all preferable changes for the whole project. Also, it is possible to use 'flake8' linter in the project.
