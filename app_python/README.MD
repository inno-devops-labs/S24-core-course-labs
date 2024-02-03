# 🇷🇺 Python web application for getting Moscow time
The main purpose of the application is to get current Moscow time in real time format. 

## Structure
The project structure organized by using two important parts

1. Frontend (written using HTML and JavaScript)
2. Backend API (written using Python with FastAPI framework)

### Server's endpoints description
Server will be located on http://127.0.0.1:8000.


Detailed description of the server could be viewed using `/docs` endpoint.

Shortly it consist of two parts
1. `/` For getting html document with the main frontend.
2. `/api/time` For getting current moscow time up to seconds.

## Installation guide
To try our service simply you can use prepared Makefile. 
Here are several commands to use
1. `make build` for creating python virtual environment and installing required dependencies.
2. `make run` for running application after installing dependencies (i.e. after using `make build`)
3. `make start` just union of two previous steps.
4. `make remove` Remove unistalled dependencies from the `make build` command.
