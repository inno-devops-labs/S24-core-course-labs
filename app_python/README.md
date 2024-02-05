# Moscow time app

## Description

A simple FastAPI app that displays Moscow time.

## Getting started

1. Install all required Python packages:

```bash
pip install -r requirements.txt
```

2. Run the application:

```bash
python main.py
```

The application will start locally on port `8000`. You can access it by navigating to `http://127.0.0.1:8000` in the web browser.

## Endpoints

A single endpoint is currently present:

- `/` (GET): Returns an HTML page with the current Moscow time.

## Templates

Jinja2 templates are used, stored in `templates` folder.

- time.html - A simple html template with the large text in the center.

## Logging

The application logs requests, returned values and errors in `app.log` file.

## Error handling
If an error occurs, the app will return a 500 status code and log an error.
