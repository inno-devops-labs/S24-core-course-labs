# Moscow Time Web App

This is a simple Flask web application that displays the current time in Moscow. It provides a basic user interface to view the current time in the Moscow timezone.

## Features

- Displays the current time in Moscow timezone.
- Built with Flask, a simple and flexible Python web framework.

## Manual set up
### Installation
1. Clone the repository:

   
    git clone https://github.com/glebuben/S24-core-course-labs.git
    
2. Navigate to the project directory:

   
    cd S24-core-course-labs/app_python
    
3. Install dependencies using pip:

   
    pip install -r requirements.txt
    
### Usage

1. Run the Flask application:

   
    python app.py
    
2. Open your web browser and go to [http://localhost:5000](http://localhost:5000) to view the current time in Moscow.

## Set up via docker
### Getting image
There are 2 possible ways to get image for this app:
1. Build it via 'Dockerfile'
```
    docker build - t <image name> app_python/
```

2. Pull from Dockerhub
```
    docker pull glebuben/dev-ops-labs:1.0
```
**Note: the image name in the second case is "glebuben/dev-ops-labs:1.0"**
### Running the image
To run the image use this command line
```
    docker run -d -p 5000:5000 <image name>
```