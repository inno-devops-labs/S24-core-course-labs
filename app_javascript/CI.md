# Node.js CI Best Practices

[![Node.js CI](https://github.com/zeyadAjamy/S24-core-course-labs/actions/workflows/javascript-ci.yaml/badge.svg?branch=lab3)](https://github.com/zeyadAjamy/S24-core-course-labs/actions/workflows/javascript-ci.yaml)

## Overview

The CI workflow is triggered on pushes to the `main` and `lab3` branches, as well as pull requests targeting these branches. It consists of three main jobs:

1. **Security**: Checks for vulnerabilities in the application dependencies using Snyk.
2. **Build and Test**: Installs dependencies, lints the code, and runs unit tests.
3. **Push Docker Image**: Builds and pushes a Docker image of the application to Docker Hub.

## Best Practices Implemented

1. **Security Checks:**
   - Integrated Snyk to identify and address vulnerabilities in Node.js dependencies.
   - Snyk is downloaded and authenticated with a secret token before running the vulnerability scan.

```yaml
- name: Snyk test
  working-directory: app_javascript
  run: |
    npm ci
    snyk auth ${{ secrets.SNYK_TOKEN }}
    snyk test --severity-threshold=high
```

2. **Dependency Management:**
   - Utilized `npm ci` for dependency installation to ensure consistent dependency resolution and faster installation times.

```yaml
- name: Install dependencies
  working-directory: app_javascript
  run: npm ci
```

3. **Code Quality:**
   - Implemented ESLint for linting to enforce coding standards and maintain consistent formatting, ensuring adherence to best practices and readability standards.

```yaml
- name: Lint code
  working-directory: app_javascript
  run: npm run lint
```

4. **Testing:**
   - Included unit tests to verify the functionality of the Node.js application, aiding in catching bugs early in the development process.

```yaml
- name: Tests
  working-directory: app_javascript
  run: npm run test
```

5. **Docker Image Management:**
   - Cached Docker image layers to expedite the Docker build process, enhancing efficiency and reducing resource consumption.

```yaml
- name: Build Docker Image
  working-directory: app_javascript
  run: docker build -t zeyadalagamy/moscow_tz_js .
```

```yaml
- name: Push Docker Image
  working-directory: app_javascript
  run: docker push zeyadalagamy/moscow_tz_js
```
