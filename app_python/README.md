# The Moscow Timezone python application

## Overview

The simple python application which display time in moscow time zone. Was built by using Flask framework.

## Installation instructions

Minimal Prerequisites:

- Python3
- pip packet manager
- Flask
- pytz library
- Docker

You can find the list of dependencies in requirements.txt file

## Environment Setup without Docker

```bash
# Navigate to the cloned Git repository folder with the source code of the tool
cd DevOps

# Navigate to the "app_python"
cd app_python

# Do not forget to run all commands in virtual environment
python3.11 -m venv env
source env/bin/activate

# Install all dependencies
pip install -r requirements.txt

# Run application
python3 time_zone.app
# or 
python time_zone.app
```

### Sample Usage

To enter the application page just open in your browser

```bash
http://127.0.0.1:5000
```


## Environment Setup with Docker
```bash
# Navigate to the cloned Git repository folder with the source code of the tool
cd DevOps

# Navigate to the "app_python"
cd app_python

# You can build your own docker image
docker build -t app_python . 

# Or pull existing one
docker pull nikitagrigorenko/app_python:latest

# Run docker image if you build your own:
docker run -p 5001:5000 app_python
# or if you pull existing one:
docker run -p 5001:5000 nikitagrigorenko/app_python:latest
```

### Sample Usage

After running a docker image open the following url in your browser:

```bash
http://127.0.0.1:5001
```


## File Structure

- `PYTHON.md`: Contains the breif explanation of best practicies while using Flask.
- `requirenments.txt`: Contains all dependencies.
- `time_zone.py`: Contains python code with Flask server and timezone of Moscow getting.
- `DOCKER.md`: Contains the breif explanation of best practicies while using Docker
- `Dockerfile`: Contains all the commands a user could call on the command line to assemble an image.
