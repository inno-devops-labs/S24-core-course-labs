# Time app

A simple app that displays a time.

Consists of two parts

1. Python API server that uses FastAPI
2. Frontend client

Server has two endpoints

1. `/` for serving static files under [./static](./static) folder
2. `/api/time?tz={tz}` route that accepts timezone and returns the time in this timezone in a format
   of `%Y-%m-%d %H:%M:%S`

Client fetches the time on interval each second.