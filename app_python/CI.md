# Continuous Integration (CI) Workflow

## Description

This document provides an overview of the Continuous Integration (CI) workflow configured for the S24-DevOps project. The CI workflow is responsible for automating the build, test, and deployment processes whenever changes are made to the main branch or pull requests are opened.

## Workflow Details

### Pipeline Description

The CI workflow is triggered on every push to the main branch and on pull requests targeting the main branch. It consists of two jobs: `build` and `docker-run`.

### Jobs

1. **build**:
   - **Runs On:** Ubuntu-latest
   - **Purpose:** This job sets up the Python environment, logs in to Docker Hub, builds the Docker image for the project, and pushes the image to the Docker registry.
   - **Steps:**
     - Checkout code from the repository.
     - Set up Python environment using the latest version.
     - Log in to Docker Hub using Docker login action.
     - Build Docker image named `time_web.py`.
     - Push Docker image to Docker Hub.

2. **docker-run**:
   - **Runs On:** Ubuntu-latest
   - **Purpose:** (Note: Description of the purpose of this job is missing in the provided YAML file. Please provide additional details if necessary.)

## Optimization Strategies

### Caching Dependencies

We leverage caching to speed up dependency installation and build steps. By caching dependencies between workflow runs, we reduce the time required for subsequent builds and ensure consistent build environments.

### Workflow Status Badge

We've added a workflow status badge to our repository README. This badge provides visibility into the current status of our CI workflow, allowing contributors to quickly assess the health of our codebase.

## Snyk Vulnerability Checks

We've integrated Snyk into our CI workflow to help us identify and address vulnerabilities in our project dependencies.

### Integration Steps

1. **Installation:** We've installed the Snyk CLI in our CI environment to facilitate vulnerability scanning of our dependencies.

2. **Authentication:** Snyk CLI is authenticated with our Snyk account to access Snyk's vulnerability database and perform scans.

3. **Vulnerability Scanning:** Snyk tests are executed as part of our CI workflow to check for vulnerabilities in our project dependencies.

4. **Handling Vulnerabilities:** Upon identifying vulnerabilities, we prioritize addressing them according to Snyk's recommendations. This may involve updating dependencies to patched versions or finding alternative solutions to mitigate security risks.

### Logging and Reporting

Snyk results are logged or reported back to our CI workflow, providing visibility into the status of vulnerability assessments. This allows us to track the resolution of vulnerabilities and maintain a secure codebase.

## Documentation

We've updated the `CI.md` file to document the structure and purpose of our CI workflow. This documentation serves as a reference for team members and contributors, providing insights into the CI pipeline's configuration and optimization strategies.

By following established CI best practices and optimizing our workflow, we aim to streamline the development process and maintain code quality and reliability.
