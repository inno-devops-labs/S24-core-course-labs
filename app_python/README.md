## Overview of project

### 1. Purpose

This simple [Python app](/app_python/)  used to display current Moscow (UTC-3) time.

### 2. Stack
- Framework: ``flask``
- Templates of pages: ``Django HTML``
- Time calculation: ``datetime`` library
- Testing: ``unittest`` library
- Logging: ``logging`` library


### 3. Structure

- ``app.py`` performs routing at ``/`` and calculates Moscow time.
- ``test_app.py`` performs unit test to validate the correctness of time.
- ``app.log`` contains logs of application during its work.

#### 3.1. Tempelates
-  ``index.html`` is the main page where time is shown.
-  ``error.html`` contains a message that error has occured.

#### 3.2. Documentation
- ``PYTHON.md`` describes the reasons of choosing ``flask`` and best practices applied to the project.
- ``README.md`` describes the overall structure of project.


### 4. Get started
- Run ``pip install -r requirements.txt``.
- Run `` python  app.py`` inside ``app_python`` folder.
- Go to ``http://127.0.0.1:5000/``.

          