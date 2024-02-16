# Moscow time web app

A web application that shows current Moscow time on the main page.

## How to run

1.  (Optional) Create a virtual environment, e.g., by running
    `python3 -m venv venv`; activate it with `source venv/bin/activate`
    (may be different for your shell).

2.  Install requirements, e.g., by running `pip3 install -r requirements.txt`
    (the requirements file is in the same directory with this file).

3.  Start the application, e.g., by running `python3 main.py`. The web application
    will become available at your `localhost` on the first free port starting with
    5000.

4.  Visit the main page, e.g., at `http://127.0.0.1:5000/` (may be different on your
    machine). Enjoy the Moscow time!

## Docker

### Build

To build, in the project directory do:

```bash
docker build . -t IMAGE_TAG_NAME
```

where `IMAGE_TAG_NAME` is the tag you want for the image.

### Pull

You can also run a pre-built version of the image. To pull it:

```bash
docker pull kolay0ne/app_py
```

Use `kolay0ne/app_py` as the image name for future docker operations.

### Run

Run a container based on the image, select options depending on your needs. For
instance, to run it in the background, exposing the port `5000` to a randomly
selected port on the host machine and automatically remove the container ones
it's stopped, do:
```bash
docker run --rm -d -p 5000 kolay0ne/app_py
```

Replace `kolay0ne/app_py` with your image/tag name if you built it manually.

## Unit Tests

To run unit tests:

-   Install `pytest` via `pip` or using your distribution-specific method

-   Go to the project directory and run the `pytest` command
