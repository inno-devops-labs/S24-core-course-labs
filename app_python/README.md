# MSK time

A python web app that shows current server time in Moscow timezone.

## Usage

Set up a virtual environment and execute these commands:

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Docker
You can run the app using docker.

### Build
```bash
docker build -t python-test-app_python .
```

Alternatively, you can pull the image from docker hub:
```bash
docker pull rinri/python-test-app_python
```

### Run
```bash
docker run -p 8000:8000 rinri/python-test-app_python:latest
```
