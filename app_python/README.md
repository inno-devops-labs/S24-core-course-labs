# My Python Web Application

## Overview
This application displays the current time in Moscow using the Flask framework.

## Features
- Displays the current time in Moscow.
- Automatically updates the time upon page refresh.

## Installation
1. Clone the repository: `git clone https://github.com/a1kuat/S24-core-course-labs.git`
2. Change into the project directory: `cd app_python`
3. Install the required packages: `pip install -r requirements.txt`
4. Run the application: `python app.py`

## Usage
Navigate to `http://localhost:5000` in your web browser to view the current time in Moscow.

## Building the Docker Image

To build the Docker image, navigate to the directory containing the `Dockerfile` and run:

`bash docker build -t my-python-app . `


## Pulling the Docker Image

The image is pushed to my Docker Hub, you can pull it using:

`bash docker pull a1kuat/my-python-app`

## Running the Docker Image

To run the Docker image locally, use:

`bash docker run -p 5000:5000 my-python-app`


Then visit `http://localhost:5000` in your web browser to see the application in action.