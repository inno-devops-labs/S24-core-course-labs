# Python Web Application Documentation

## Description
This Python web application displays the current time in Moscow. It was developed using Flask framework, following best practices and coding standards.

## Features
- Displays the current time in Moscow.

## Framework Used
- Framework: Flask
- Justification: Flask was chosen for its simplicity, flexibility, Pythonic nature, and suitability for smaller web projects.


## Installation and running locally
1. Clone the repository:
 ```bash
   git clone <repository-url>
 ```
2. Install dependencies:
 ```bash
   pip install -r requirements.txt
 ```
3. Run the application:
```bash
    python app.py
 ```

## Docker
This application is containerized using Docker for easy deployment and portability.
### Instructions for execution

1. Building the Image:
   ```bash
   docker build -t my-app .
   ```

2. Pulling the Image (Optional if not built locally):
   ```bash
   docker pull anastasiamartynova/my-docker-repo:latest
   ```

3. Running the Container:
   ```bash
   docker run -p 8080:8080 anastasiamartynova/my-docker-repo:latest
   ```


## File Structure

- `app.py`: Main Flask application file.
- `requirements.txt`: Python packages with their versions necessary for running the application.
- `PYTHON.md`: Explains Flask choice; covers coding standards & testing.

