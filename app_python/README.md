# Moscow Time Web Application
### Features

- Root Endpoint (`/`): Displays the current time in Moscow.
- Visits Endpoint (`/visits`): Displays the total number of visits.

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

## Unit Tests
### Test Descriptions
 `test_current_time_displayed `: Verifies that the current time in Moscow is displayed on the page and the correct template index.html is used.

 `test_time_zone_offset `: Confirms that the time shown has a +3-hour offset, representing Moscow time.

 `test_content_contains_date `: Checks that the page includes the current date in the YYYY-MM-DD format.
 
## Running the Tests
 
To run the unit tests, use the following command:

```bash
python -m unittest test_app.py
```
## Continuous Integration (CI) Workflow
This project uses GitHub Actions for Continuous Integration (CI), ensuring the reliability and quality of the code with each update. The CI workflow is triggered on every push or pull request to the main branch.

## CI Workflow Steps
1. Dependencies: Installs Python dependencies specified in `requirements.txt` using pip.
   
2. Linter: Checks code style with `flake8`, enforcing PEP 8 standards and improving code readability and consistency.
   
3. Unit Tests: Runs a suite of unit tests located in the `app_python` directory to ensure that individual parts of the application work as expected.
   
4. Docker Build: Builds a Docker image for the application within the CI environment.

This CI setup ensures that code is linted, tested, and that Docker images are built successfully with each change, allowing for consistent and reliable updates. The workflow file is located in `.github/workflows/ci.yml`.