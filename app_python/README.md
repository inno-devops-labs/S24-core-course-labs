# Python Web Application

A Web Application that displays current time in Moscow based on Google NTP service (since the system may have incorrect time set)

## Installation and Running

```bash
 python -m venv venv
 ./venv/Scripts/activate
 pip install -r requirements.txt
 cd app
 sanic server:app
```

If everything goes well, you will see startup logs with message`Starting worker [...]`. You can now see html page with moscow time at `localhost:8000`

## Docker

### How to build

```bash
cd app_python
docker build -t tufra/moscow-time-app .
```

### How to pull

```bash
docker image pull tufra/moscow-time-app-python
```

### How to run

```bash
docker run -p 80:8080 -t tufra/moscow-time-app-python
```

Now you can see moscow time at `localhost`
