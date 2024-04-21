# Moscow time server

[![app python](https://github.com/MasterLogick/S24-core-course-labs/actions/workflows/docker.yaml/badge.svg?branch=lab03)](https://github.com/MasterLogick/S24-core-course-labs/actions/workflows/docker.yaml)

This service shows current time in Moscow zone.

Check `/visits` to get total visits count for the website.

## Setup

```bash
#Create python venv
python3 -m venv venv

#Activate venv
source venv/bin/activate

#Install all required packages
pip3 install -r requirements.txt
```

## Run

```bash
#Activate venv
source venv/bin/activate

#Start server
python3 main.py
```
