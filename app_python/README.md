# Time API 
A simple web api returning value of time

## Description
A python application that returns current time value (by default in Europe/Moscow timezone)

## Getting Started

### Dependencies
#### Necessary
* Python 3.8.9 and higher
* pip 21.3.1 and higher 
#### Desirable 
* Linux or macOS (for accuracy of the "How to run" instruction)

## How to run 
* move to the `app_python/app` dir 
```bash
cd app_python/app 
```
* install dependencies 
```bash 
pip install -r requirements.txt
```
* run the flask application 
```bash
flask --app main run
```

## How to use 
### API use 
There is a single HTTP endpoint: 
* `/api/v1/time` 
It returns either one of: 
  * Response code 200: `{"time": "time-placeholder"}`
  * Response code 500: `{"error": "Internal Server Error"}`
### Configuration 
You can configure the app setting the following env variables: 
* `PORT` - number of port used by the app (default - 5000)
* `TIMEZONE` - timezone of the time returned (default - 'Europe/Moscow')
* `DATETIME_FORMAT` - Python format datetime returned by the app (default - '%Y-%m-%d %H:%M:%S %z')

