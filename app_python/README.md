## Overview

This simple Python web application is built using the FastAPI framework to display the current time and date in Moscow.
For now you have to refresh the browser page manually to update the time.

## Dependencies

**FastAPI:** FastAPI is used as the web framework for building the API endpoints.  
**Pytz:** Pytz is used for working with timezones and getting the current time in Moscow.  
**Uvicorn:** Uvicorn is used as the ASGI server to run the FastAPI application.

## How to run

1. Install the required dependencies by running:
   ```bash
   pip install -r requirements.txt
   ```
2. Navigate to the project directory containing `main.py`.
3. Run `main.py` to start the FastAPI server:
    ```bash
    python main.py
    ```
4. Open a web browser and navigate to `http://127.0.0.1:8000`

## Template

A small `index.html` template is used to better visualize the current time in Moscow in the browser.

## Docker

### How to build

To build the Docker image, move to the app_python directory:
```bash
cd .\app_python\
```

and execute the following command to create a docker image:

```bash
docker build -t monykekker/my_app .
```

### How to pull?
You can pull already existing image using this command:
```bash
docker pull monykekker/my_app:latest
```

### How to run?
To run the Docker container, execute the following command:
```bash
docker run -p 8000:8000 monykekker/my_app
```
Then go to the [localhost:8000](http://localhost:8000/) to see Moscow time.