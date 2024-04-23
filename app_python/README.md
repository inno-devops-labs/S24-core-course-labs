![example workflow](https://github.com/Antony-Sk/S24-DevOps-labs/.github/workflows/python.yml/badge.svg)

## Python web app

This is simple python flask web application for obtaining current time in Europe/Moscow timezone

Install dependencies:
```bash
pip install -r requirements.txt
```
Start server:
```bash
python main.py
```
This will start a local web server, and you can access the current time in Moscow by going to http://127.0.0.1:5000/ in your web browser.

Example result:
```The current time in Moscow is 2024-02-06 15:40:22```

Also, you can see number of visits of site on GET http://127.0.0.1:5000/visits

Example result:
```{visits:2}```



Additionaly you can run unittests by command:
```bash
pytest test.py
```

### Running with docker

You may use already built image:

```bash
docker pull pgrammer/app_python
docker run -p 5000:5000 pgrammer/app_python
```

Or build it yourself:

```bash
docker build -t app_python .
docker run -p 5000:5000 app_python
```

Now you can see Moscow time at http://localhost:5000

### Unit Tests

You can run unit tests with:
```bash
pytest test.py
```
### CI Workflow

I use GitHub Actions workflow to automate testing, security scanning of my app

It uses GitHub Action on push requests

On build: It uses python3.9, installs dependencies from `requirements.txt`, and run `flake8` for linting purposes

On security: It uses SNYK to check on vulnerabilities

On Docker: It sets p Docker service and builds image from `<docker_id>/app_python:latest`
