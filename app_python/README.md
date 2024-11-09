# Moscow Time Web Application

## Overview

This is a simple Flask web application that displays the current time in Moscow. It uses Flask to handle routing, `pytz` to manage timezone conversions, and serves a static image from the `/static` folder. The app is lightweight and demonstrates basic Flask functionality.

## Run the project locally
```bash
git clone https://github.com/eeetaF/S24-devops-labs/tree/lab1
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py
# follow http://127.0.0.1:5000/
```

## How to Build the Docker Image
### 1.1 Build the application
```bash
docker build -t <dockerhub_username>/moscow-time-app .
``` 
### 1.2 Or pull the application from dockerhub (you may use my public image by entering "Fatee" as <dockerhub_username>)
```bash
docker pull <dockerhub_username>/moscow-time-app:latest
```
### 2 Run the Docker Container
```bash
docker run -p 5000:5000 <dockerhub_username>/moscow-time-app
```
### *3 Stop the Docker Container
```bash
docker ps
```
```bash
docker stop <container_id>
```
### *4 Remove the Docker Container
```bash
docker rm <container_id>
```
### *5. Remove the Docker Image
```bash
docker rmi <dockerhub_username>/moscow-time-app
```