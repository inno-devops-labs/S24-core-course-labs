# Simple Flask app
The idea of the app is really simple, it just shows the current time in Moscow

# Set up
1. Firstly it is preferable to use virtual environment for `python`:
```bash
python3 -m venv env
```
2. Activate the virtual environment
```bash
source env/bin/activate
```
3. Install dependencies
```bash
pip install -r requirements.txt
```
4. Run the application
```bash
python app.py
```
- Directly (using python)
```bash
python app.py
```
- Using docker image (see below)

# Testing
All tests can be found in the directory `tests`, to run them use the following command:
```bash
pytest tests/*.py
```

# Stack
- Python
- Flask
- Pytests
- BeautifulSoup (for tests)
- Requests (for tests)
– Logging (standard library)

# Docker
## Build
To build docker image you can use the following command:
```bash
docker build -t {docker_image_name} .
```
for example:
```bash
docker build -t anton_flask .
```

## Pull
To pull this image from Docker hub [link](https://hub.docker.com/repository/docker/nad777/anton_nekhaev_flask/general). You can use the following command:
```bash
docker pull nad777/anton_nekhaev_flask:latest
```
## Run
To run you docker image after build you need to use the following command:
```bash
docker run -p 5000:5000 {docker_image_name}
```
for example:
```bash
docker run -p 5000:5000 anton_flask
```
**OR** (if you pull from Docker hub)
```bash
docker run -p 5000:5000 nad777/anton_nekhaev_flask:latest
```
