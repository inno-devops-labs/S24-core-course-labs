# Python Web Application

![CI](https://github.com/habur331/S24-DevOps-course-labs/actions/workflows/main.yml/badge.svg)
## Overview

This document outline a simple Python web application designed to display the current time in Moscow. The application leverages the Flask framework, adhering to established best practices and coding standards.

## Features

- Displays the current time in Moscow on endpoint "/"
- Stores number of accesses to endpoint "/". Its accessible on endpoint "/visits". Number is persistent between restarts   

## Testing Best Practices

### Manually Testing

The application shows current time in Moscow correctly on reloading main page.

## Getting Started

### Installation

1. Clone the Repository

2. Install dependencies:requirements
```bash
   pip install -r requirements.txt
``` 
3. Run Flask Server

### Unit Testing
`unittest` is used for unit testing. In order to run tests the following command can be used

```bash
python -m unittest discover -s app_python
```

### Docker

- You can build image on your own
```bash
docker build . -f Dockerfile -t habur331/devops-course
```

- Or can pull image from DockerHub
```bash
docker pull habur331/devops-course:latest
```
- Run container
```bash
docker run -dp 5000:5000 habur331/devops-course:latest
```
- Access app on http://localhost:5000