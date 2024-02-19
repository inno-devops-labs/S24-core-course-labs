# Flask MSK Timezone Web Application

## Introduction

This Flask application provides a simple web service to display the current time in the Moscow (MSK) timezone. It utilizes the Flask micro-framework for Python and the pytz library for timezone handling.

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   ```

2. Navigate to the project directory:

   ```bash
   cd app-python
   ```

3. Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask application:

   ```bash
   python3 app.py
   ```

2. Access the web service:

   Navigate to `http://127.0.0.1:5000/msk_timezone` in your web browser. You should see the current time in the Moscow timezone displayed.

## File Structure

- `app.py`: Contains the main Flask application code, including the route for fetching the current time in the Moscow timezone.
- `requirements.txt`: Lists the required Python packages and their versions for running the application.
- `PYTHON.md`: Justifies the choice of Flask framework and describes best practices applied in the web application, including coding standards, testing, and code quality.

## Additional Information

- **Flask Version**: 3.0.2
- **pytz Version**: 2024.1

# Unit testing
- unittest was used for testing
- A useful feature of unittest is automated testing.
- One can collect tests into groups
- Collect test execution results (for example, for a report).
- OOP style allows you to reduce code duplication in case of similar test objects

# Continuous Integration (CI)

This project utilizes Continuous Integration (CI) to automate the build, test, and deployment processes using GitHub Actions. The CI workflow ensures that code changes are thoroughly tested and verified before being merged into the main branch.

## Workflow Details

The CI workflow consists of the following essential steps:

- **Dependencies**: Installs project dependencies using pip.
- **Linting**: Runs Flake8 to check for code style and potential errors.
- **Testing**: Executes unit tests to ensure code correctness.
- **Docker Integration**: Builds a Docker image of the application and pushes it to DockerHub.

## Branches

The CI workflow is triggered on all branches and pull requests to the main repository. This ensures that changes made to the codebase are continuously integrated and validated across all branches.

## DockerHub Integration

To enable DockerHub integration, ensure that the following secrets are configured in your GitHub repository settings:

- `DOCKER_USERNAME`: Your DockerHub username.
- `DOCKER_PASSWORD`: Your DockerHub password or access token.

These secrets are securely used by the CI workflow to log in to DockerHub and push Docker images generated during the build process.

## Viewing Workflow Runs

You can view the details and status of CI workflow runs by navigating to the "Actions" tab in your GitHub repository. The workflow status badge above provides a quick visual indicator of the latest workflow run status.

## Contributing

Contributions to the project are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request. All contributions undergo automated testing and review through the CI workflow to maintain code quality and stability.
