# Current Moscow Time

[![Python web application][badge]][workflow]

[badge]: https://github.com/SnejUgal/S24-core-course-labs/actions/workflows/python.yaml/badge.svg

A simple web application that shows the current time in Moscow.

```
$ curl localhost:8080
2024-02-05T21:58:51.772798+03:00
```

The app also tracks how many times it was accessed.

```
$ curl localhost:8080/visits
9
```

## Installation

Ensure that you have Python 3 installed. After that, install the required
packages using `pip`, possibly inside a virtual environment.

```bash
pip3 install -r requirements.txt
```

## Running

```bash
python3 src/main.py
```

If everything is okay, you'll see the following output. Now you can make
requests to `localhost:8080` to fetch the current Moscow time.

```
======== Running on http://0.0.0.0:8080 ========
(Press CTRL+C to quit)
```

## Docker

You can also use a Docker container with this app. If you want to build a new
image for this app, run

```bash
docker build -t devops .
```

Alternatively, you can pull an already-built image from Docker Hub. Download it
by running

```bash
docker pull snejugal/devops-lab2
```

Once you obtain the image, run it using

```bash
docker run --rm -p 8080:8080 -v ./data:/app/data -d snejugal/devops-lab2
chmod a+w data
```

## Testing

To run tests for the application, run

```
pytest src/test.py
```

## CI

This reposity has a CI workflow which automatically runs tests for this
application and updates the app's image on Docker hub. See the [workflow] for
more.

[workflow]: ../.github/workflows/python.yaml
