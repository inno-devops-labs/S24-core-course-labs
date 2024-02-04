# Moscow Time Flask Web Application Documentation

## Description

This application is a simple Flask web service that displays the current time in Moscow. It uses the pytz library to
handle timezone conversions and the Flask framework for rendering the webpage.

## Installation

To set up this application, you will need to install the Flask framework and the pytz library. Ensure you have Python
3.9 installed on your machine.

1. Clone the repository

2. Navigate to the project directory:

    ```bash
    cd app_python
    ```

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:

    ```bash
    python app.py
    ```

## Usage

Once the app is running, you can access the web service by navigating to <http://localhost:5000/> in your web browser. You
will see the current time in Moscow automatically updating every second.

## Testing

Run the unit tests with the following command:

```bash
python test_app.py
```

## Deployment

For production deployment, set the debug option to False and configure the application to be hosted on a web server such
as Nginx or Apache with a WSGI server like Gunicorn.

```python
if __name__ == '__main__':
    app.run(debug=False)
```

Ensure to use environment variables for configuration settings and secrets management in a production environment.
