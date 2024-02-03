# Moscow Time Web Application

This simple Python web application built with Flask displays the current time in Moscow.

## Usage

1. Install dependencies using `pip install -r requirements.txt`.
2. Run the application using `python main.py`.
3. Open your web browser and go to `http://127.0.0.1:5000/` to view the Moscow time.

## Project Structure

- `app_python/`: Main application folder.
  - `main.py`: Flask application.
  - `templates/`: HTML templates.
  - `requirements.txt`: Python app requirements.

## Docker

### Build the Docker Image

```bash
docker build -t flask-moscow-time-app .
```

### Pull the Docker Image

```bash
docker pull evsey/flask-moscow-time-app:latest
```

### Run the Docker Image

```bash
docker run -p 5000:5000 evsey/flask-moscow-time-app
```
