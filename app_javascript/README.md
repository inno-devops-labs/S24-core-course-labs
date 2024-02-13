# Moscow Time Web Application

## Overview

The Moscow Time Web Application is a simple JavaScript-based web application that displays the current time in Moscow. It provides users with an easy and quick way to check the current time in the Moscow timezone.

## Features

- Lightweight and minimalistic design for a seamless user experience.
- Responsive layout for compatibility across various devices and screen sizes.

## Framework and Technologies

The application is built using Javascript programming language and using express framework.

The decision to avoid additional frameworks was made to keep the application lightweight and easily understandable for developers of all experience levels.

## Installation and Usage

1. Clone or download the repository to your local machine.
2. Install Node.js on your system
3. Run the server using the command ```node app.js```
4. Open a web browser and visit `http://localhost:3000/` to access the application.
5. The web page will display the current time in Moscow.


## Docker Containerization

### Building the Docker Image

To build the Docker image locally, execute the following command in the root directory of the project:

```bash
docker build -t your_username/app_js .
```

Replace `your_username` with your Docker Hub username. This command will create a Docker image with the tag latest.

### Pulling the Docker Image

To pull the image from docker hub, you can use the following command:

```bash
docker pull your_username/app_js:latest
```

### Running the Docker Image
To run the Docker container and start the application, use the following command:

```bash
docker run -p 3000:3000 your_username/app_js:latest
```
<n><n>
Please note that you must have docker installed on your device to be able to run the previous commands.