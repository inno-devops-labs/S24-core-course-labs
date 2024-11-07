# Moscow Time Web Application

## Getting Started

### Prerequisites

- Python 3.x
- Pip (Python package installer)
- Docker

### Installation


1. Install dependencies:

```bash  
pip install -r requirements.txt
```

## Docker Container

### How to Build the Docker Image

1. Navigate to the `app_python` folder:

```bash 
cd moscow-time-web-app/app_python
```

2. Build the Docker image:

```bash 
docker build -t moscow-time:latest .
```
    
### How to Run the Docker Container

1.  Run the Docker container:
    
```bash 
docker run -p 5000:5000 moscow-time:latest
```
    
2.  Open your web browser and navigate to [http://localhost:5000/](http://localhost:5000/) to view the current Moscow time.

## Building and running docker

To run the application as docker container:

```bash
docker pull aximaxxi/moscow-time:latest
```

```bash
docker run -p 5000:5000 aximaxxi/moscow-time:latest
```

After running this command, the Flask application will be accessible at http://localhost:5000.