# CI Best Practices

[![Python CI](https://github.com/zeyadAjamy/S24-core-course-labs/actions/workflows/python-ci.yaml/badge.svg?branch=lab3)](https://github.com/zeyadAjamy/S24-core-course-labs/actions/workflows/python-ci.yaml)

## Overview

The CI workflow is triggered on pushes to the `main` and `lab3` branches, as well as pull requests targeting these branches. It consists of three main jobs:

1. **Security**: Checks for vulnerabilities in the application dependencies using Snyk.
2. **Build and Test**: Installs dependencies, lints the code, and runs unit tests.
3. **Push Docker Image**: Builds and pushes a Docker image of the application to Docker Hub.

## Best Practices Implemented

### 1. Security Checks

- **Snyk Integration**: The workflow integrates Snyk to identify and address vulnerabilities in the Python dependencies. Snyk is downloaded and authenticated with a secret token before running the vulnerability scan.

### 2. Dependency Management

- **Dependency Caching**: Dependencies are cached to improve workflow efficiency and reduce build times. This is achieved using GitHub Actions cache feature, ensuring that dependencies are only reinstalled when necessary.

```yaml
# Example:
build:
  steps:
    - uses: actions/cache@v2
      with:
        path: /home/runner/.cache/pip
        key: ${{ runner.os }}-pip-${{ hashFiles('app_python/requirements.txt') }}
        restore-keys: |
          ${{ runner.os }}-pip-
```

### 3. Code Quality

- **Linting**: The code is linted using Black and Flake8 to enforce coding standards and maintain consistent formatting. Black is used for code formatting, while Flake8 is used for static code analysis to identify potential issues and ensure adherence to PEP 8 guidelines.

```yaml
# Example:
lint:
  steps:
    - name: Lint code
      working-directory: app_python
      run: |
        black . --line-length=79
        flake8 .
```

### 4. Testing

- **Unit Tests**: The workflow includes unit tests to verify the functionality of the Python web application. These tests ensure that the application behaves as expected and help catch bugs early in the development process.

```yaml
# Example:
tests:
  steps:
    - name: Tests
      working-directory: app_python
      run: |
        pytest .
```

### 5. Docker Image Management

- **Docker Image Caching**: Docker image layers are cached to speed up the Docker build process. This is achieved using GitHub Actions cache feature, which stores Docker layers and retrieves them for subsequent builds.

```yaml
# Example:
push-docker:
  steps:
    - uses: actions/cache@v2
      with:
        path: /tmp/.buildx-cache
        key: ${{ runner.os }}-docker-${{ hashFiles('app_python/**/Dockerfile') }}
        restore-keys: |
          ${{ runner.os }}-docker-
```

### 6. Workflow Optimization

- **Working Directory**: Each step in the workflow operates within the `app_python` directory, ensuring that commands are executed in the correct context and dependencies are installed and tested within the application directory.

```yaml
# Example:
lint:
  steps:
    - name: Lint code
      working-directory: app_python
      run: |
        black . --line-length=79
        flake8 .
```

- **Efficient Docker Build**: Docker build and push steps are optimized by caching Docker layers, reducing build time and resource consumption.

```yaml
# Example:
push-docker:
  steps:
    - uses: actions/cache@v2
      with:
        path: /tmp/.buildx-cache
        key: ${{ runner.os }}-docker-${{ hashFiles('app_python/**/Dockerfile') }}
        restore-keys: |
          ${{ runner.os }}-docker-
```
