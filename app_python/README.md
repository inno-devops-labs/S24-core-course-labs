# Moscow Time Web App 🌍🕒

Welcome to the Moscow Time Web Application! This Python-based web app elegantly displays the current Moscow time. Before running the application, make sure to check and install the required packages listed in `requirements.txt`.

## How to Run

Follow these simple steps to get the Moscow Time Web App up and running on your Microsoft, Linux, or MacOS system:

1. **Check Requirements:**
   Before diving in, ensure you have all the necessary packages installed. You can quickly install them by running the following command in your terminal:

    ```bash
    pip install -r requirements.txt
    ```

2. **Run the Program:**
   Once the requirements are set, fire up the application by running the following command in your terminal:

    ```bash
    python3 app.py
    ```

3. **Access the Website:**
   After successfully running the program, open your preferred web browser and enter the following URL:

    ```
    http://127.0.0.1:5000
    ```

   You're now in sync with Moscow time.

**Note:** Ensure you are in the correct path before running the application to experience Moscow time seamlessly. Enjoy your time-traveling journey! ⏰✨

## Docker

### Overview
This application can also be run as a Docker container, making it easy to deploy and run in any environment that supports Docker containers.

### How to Build
To build the Docker image for this application, follow these steps:
1. Make sure you have Docker installed on your system.
2. Navigate to the directory containing the Dockerfile and application files.
3. Run the following command to build the Docker image:

    ```bash
    docker build -t moscow-time-app .
    ```

### How to Run
To run the application using the Docker image you built, execute the following command:

```bash
    docker run -p 5000:5000 moscow-time-app
```
### Unit Tests

We have comprehensive unit tests for this application to ensure its correctness. Check the PYTHON.md file for details on the implemented unit tests and best practices applied.