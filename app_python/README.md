# Flask Web Application displaying current time in Moscow

## Description

This is a simple Flask web application that displays the current time in Moscow.

## Structure

- `app.py` - the main application file.
- `requirements.txt` - the list of required Python packages.
- `templates` - the directory containing HTML templates.
  - `base.html` - the base HTML template.
  - `moscow_time.html` - the template for the main page.
- `static` - the directory containing static files.
  - `style.css` - the CSS file for the application.
- `tests` - the directory containing tests.
  - `unit` - the directory containing unit tests.
  - `test_moscow_time.py` - the unit test for the application.

## How to Run

1. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

2. Run the application:

    ```bash
    python app_python/app.py
    ```

3. Open the web browser and navigate to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to see the current time in
   Moscow.

## How to Test

1. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

2. Run the tests:

    ```bash
    python app_python/tests/unit/test_moscow_time.py
    ```

## Author

Created by Lev Rekhlov, B21-DS-02, [l.rekhlov@innopolis.university](mailto:l.rekhlov@innopolis.university)
