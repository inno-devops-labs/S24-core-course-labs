# Motivational Quotes Web App

This repository contains a Node.js web application built with Express that displays a random motivational quote each time the page is refreshed. It's designed to demonstrate the development of a simple web application using Express and best practices in JavaScript development.

## Overview

The application serves a single route that randomly selects a quote from a predefined list and displays it to the user. It showcases the use of basic Express setup, route handling, and sending HTML responses to the client.

## Local Installation

To run this application locally, follow these steps:

1. **Clone the Repository**:
```bash
git clone https://github.com/LaithAlebrahim/S24-core-course-labs.git
```

cd app_js


2. **Install Dependencies**:
```bash
npm install
```

3. **Run the Application**:
```bash
node app.js
```


4. **View in Browser**:
Open `http://localhost:3000/` in your web browser to view the application.

## Features

- Simple Express setup.
- Random quote generation.
- Basic HTML response.



## Docker Container
To simplify deployment, the application has been containerized with Docker. Follow these steps to run the app using Docker:
1. **Build the Docker Image locallu:**:
```bash
docker build -t AlebrahimLaith/app_js:latest .
```
2. **Run the Docker Container:**:
```bash
docker run -p 3000:3000 AlebrahimLaith/app_js:latest
```
3. **Access the application:**:
Open a browser and go to http://localhost:3000/ to view the application.

Or

2. **Pull the Docker image directly from Docker Hub:**
  ```bash
    docker pull AlebrahimLaith/app_js:latest

    docker run -d -p 3000:3000 AlebrahimLaith/app_js:latest
  ```
2. **Run the Docker Container:**:
```bash
docker run -p 5000:5000 AlebrahimLaith/app_js:latest
```
Open a browser and go to http://localhost:3000/ to view the application.