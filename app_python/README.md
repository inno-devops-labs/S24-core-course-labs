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

If everything goes well, you will see startup logs with message`Starting worker [...]`. You can now see an html page with moscow time at `localhost:8000`