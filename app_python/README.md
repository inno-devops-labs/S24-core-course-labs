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

## Quality checking 
To check the quality of the written code, it is possible to commit changes and run `pre-commit` command. It will show all preferable changes for the whole project. Also, it is possible to use 'flake8' linter in the project.
