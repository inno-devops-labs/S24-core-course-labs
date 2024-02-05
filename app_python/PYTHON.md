# My application implementation info 

* ## Chosen framework
  For my app implementation, I decided to use [Flask](https://flask.palletsprojects.com/en/3.0.x/) framework since it is the easiest framework for web development in Python. Moreover, it suits app needs:
  * easy to understand: firstly, I wanted to choose [Django](https://www.djangoproject.com/) framework, but I understood that creating an app in Django takes much more time rather than in Flask;
  * has good documentation: it took 20-30 minutes for me to develop the whole app from scratch, I have never used Flask before;
  * has a logging system.
  Of course, Flask has some disadvantages compared to Django such as scalability, however, for this project Flask functionality is more than enough.

* ## Best practices applied
  I followed the following practices:
    1. Flask framework usage;
    2. PEP8 style guide for Python;
    3. proper variables names;
    4. proper documentation: I wrote documentation for all functions;
    5. virtual environment usage;
    6. testing: I implemented several [tests](https://github.com/SokolOFFF/S24-DevOps/blob/lab01/app_python/PYTHON.md#testing) to test the whole app;
    7. proper project structure: `src/` for codes, `tests/` for test;
    8. use of `requirements.txt` and `.gitignore` files in the development;
    9. [linter](https://github.com/SokolOFFF/S24-DevOps/blob/lab01/app_python/PYTHON.md#linter) usage;
    10. proper commits names.

* ## Testing
  For proper app testing, I used [pytest](https://docs.pytest.org/en/8.0.x/). Overall I wrote 5 tests:
    * correct `unify_number()` implementation in `src/app.py` | test implemented in `tests/test_app_calculations_functions.py`;
    * correct response status while connecting to `/` route | test implemented in `tests/test_app_responses.py`;
    * the time, shown on the page is correct (comparing response text with the current time) | test implemented in `tests/test_app_responses.py`;
    * the date, shown on the page is correct (comparing response text with the current date) | test implemented in `tests/test_app_responses.py`;
    * the time on the page updates after the page refreshing | test implemented in `tests/test_app_responses.py`.

  Best practices for testing which I applied:
    * testing framework usage: I used pytest;
    * clear and descriptive test names and comments;
    * small, focused tests that cover specific functionality or behavior;
    * assertions usage to check that the code under test produces the expected results;
    * one test tests one functionality.
 
* ## Linter
    I was developing the app in the PyCharm, which already has [flake8](https://github.com/PyCQA/flake8) and [pylint](https://pypi.org/project/pylint/) linters, however, I decided to install flake8 to my project and run it each time before committing with [pre-commit](https://pre-commit.com/) tool. Config for 'pre-commit' is written in `./pre-commit-config.yaml` file.
  
