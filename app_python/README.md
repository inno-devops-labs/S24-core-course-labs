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
## Continuous Integration (CI) Workflow

Our project leverages GitHub Actions for Continuous Integration to ensure that every change made to the codebase is automatically built, tested, and ready for deployment. Here's a breakdown of the key steps in our CI workflow:

### Steps in CI Workflow

1. **Install Dependencies:**
   - This step checks and installs the necessary Python dependencies specified in `requirements.txt`. It ensures that our project has all the required libraries to build and run successfully.

2. **Run Linter:**
   - We use Flake8 to perform linting checks on the code. This step helps in maintaining code quality and consistency by identifying stylistic errors, programming errors, and complex or bug-prone constructs.

3. **Execute Tests:**
   - Our CI workflow runs a suite of unit tests to verify the application's functionality. It ensures that new changes do not break existing functionality and that new features work as expected.

### Docker Integration

In addition to the basic CI steps, our workflow includes Docker-related steps to containerize the application, making it easy to deploy and run in any environment that supports Docker.

1. **Docker Login:**
   - This step involves logging into Docker Hub (or any other Docker registry you use) to allow the subsequent push of the Docker image. It uses secrets stored in GitHub Actions to securely authenticate.

2. **Build and Push Docker Image:**
   - After successful login, the workflow builds the Docker image for the application, tagging it appropriately. Following the build, the image is pushed to Docker Hub, making it available for deployment.

### Workflow File

For a detailed look at the CI workflow, including the exact commands and configurations used, please refer to the `.github/workflows/main.yml` file in our repository. This file contains the YAML definitions for all the steps mentioned above, along with additional configurations for triggers, environment variables, and more.

### Benefits

This CI workflow ensures that our application is always in a deployable state. It improves the quality of our code, makes our development process more efficient, and significantly reduces the chances of integration problems at a later stage.

For contributors, this means that you can submit pull requests with confidence, knowing that your code will be automatically checked for integration and quality issues.

---

By implementing these CI practices, we aim to maintain high standards of quality and reliability for the Moscow Time Web App, ensuring a seamless experience for both developers and users.
