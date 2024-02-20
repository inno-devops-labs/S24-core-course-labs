# Moscow time app

## Description

A simple Express.js app that displays Moscow time.

## Getting started

1. Install `Express.js` framework:

```bash
npm install express
```

2. Run the application in the root folder:

```bash
node app.js
```

The application will start locally on port `3000`. You can access it by navigating to `http://127.0.0.1:3000` in the web browser.

## Endpoints

A single endpoint is currently present:

- `/` (GET): Returns an HTML page with the current Moscow time.

## Templates

Templates are stored in `views` folder.

- time.html - A simple html template with the large text in the center.

## Logging

The application writes the logs into console

## Error handling
If an error occurs, the app will log an error.

## Docker

To build an image, run the following command in `app_javascrpit` directory of the project:

```bash
docker build -t moscow-time-app-js .
```

Alternatively, you can pull the image from `dockerhub`:

```bash
docker pull damirafliatonov/moscow-time-app-js:latest
```

To run the image, run the following command:

```bash
docker run -p 3000:3000 moscow-time-app-js
```

After that, the application will be accessible at `http://localhost:3000/` in the web browser.


## Unit tests
Unit tests are located inside the `tests/unit/test.py` file. They can be run using `pytest`:

```bash
pytest tests/unit/test.py
```

## CI workflow

At push/pull request into `app_javascript`, workflow starts via github actions. It runs dependencies check, linter and tests of the project. Moreover, the docker image is built and pushed into the Dockerhub.
