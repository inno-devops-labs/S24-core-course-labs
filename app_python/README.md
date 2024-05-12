# Python Web Application - Current Time in Moscow

## Description
This Python web application displays the current time in Moscow. It is a simple Flask application that fetches the current time in the Moscow timezone using the datetime and pytz libraries.

## Installation
1. Clone the repository to your local machine:
   ```
   git clone <repository_url>
   ```
2. Install the required dependencies using the requirements.txt file:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Run the Flask application by executing the following command in your terminal:
   ```
   python app.py
   ```
2. Access the web application in your browser at http://localhost:5000/ to view the current time in Moscow.

## App.py Code Explanation
1. The code fetches the current time in Moscow timezone using the pytz library.
2. If successful, it returns the current time in Moscow as a response.
3. If an error occurs, it returns an error message.

## Error Handling
The application includes error handling to manage exceptions and provides an error message if any issues occur.

## .gitignore
The .gitignore file is included to ensure that unnecessary files and directories are not pushed to the repository.

## requirements.txt
The requirements.txt file lists the necessary dependencies for the application to function correctly.

## Technologies Used
- Python
- Flask
- pytz
- datetime

## Docker

### Building the Docker Image
To build the Docker image for this application, follow these steps:
```bash
docker build -t app_python .
```

### Pulling the Docker Image
To pull the Docker image from Docker Hub, use the following command:
```bash
docker pull {your_username}/app_python
```

### Running the Docker Container
To run the Docker container for the application, execute the following command:
```bash
docker run -d -p 5000:5000 {your_username}/app_python
```

Access the web application in your browser at http://localhost:5000/ to view the current time in Moscow within the Docker container.

## Unit Tests
The application includes unit tests to verify the functionality of the time retrieval and response formatting. The tests ensure that the response contains the expected time message and that the time format is correct.

To run the unit tests:
```bash
pytest test_app.py
```

## CI Workflow

### Workflow Description
The CI workflow for this project is set up using GitHub Actions. It includes the following essential steps:
- **Dependencies:** Installs project dependencies specified in `requirements.txt`.
- **Linter:** Runs pylint to check code style.
- **Tests:** Executes unit tests using pytest.
- **Docker Steps:**
  - **Login to Docker Hub:** Authenticates with Docker Hub using GitHub Secrets.
  - **Build and Push Docker Image:** Builds the Docker image for the application and pushes it to Docker Hub.

### Running the Workflow
The CI workflow runs on push and pull requests to the repository. It checks the code dependencies, style, and tests on each commit.
