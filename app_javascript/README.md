# ToDo List App

A simple ToDo List web application built with Node.js and Express.

## Setup

### Prerequisites

- Node.js installed on your machine
- npm (Node Package Manager)

### Installation

1. Clone the repository:

   ```bash
   git clone -b lab01 https://github.com/bruteforceboy/S24-core-course-labs/
   ```
2. Navigate to the project directory:
   ```bash 
   cd S24-core-course-labs/app_javascript/
   ```
3. Install dependencies:
   ```bash 
   npm install
   ``` 
4. Run the application: 
   ```bash 
   node app.js
   ```
   ![alt text](./md_screenshots/image.png)
5. Unit Tests: 
   ```bash
   npm test
   ``` 

## Docker 

### Building the Docker Image (Locally)

1. **Building the image**
   ```bash 
   docker build -t app_javascript .
   ```
2. **Running the container at [localhost:5001](127.0.0.1/5001)**
   ```bash 
   docker run -d -p 5001:5001 --name app_javascript_container app_javascript
   ```

### Building the Docker Image (Docker Hub)

1. **Building the image**
   ```bash 
   docker pull cogbonna/app_javascript_image
   ```
2. **Running the container at [localhost:5001](127.0.0.1/5001)**
   ```bash 
   docker run -dp 0.0.0.0:5001:5001 cogbonna/app_javascript_image
   ```

## CI Workflow

This CI workflow is responsible for building, testing, ensuring security, and deploying the JavaScript application. Below are the details of the workflow:

### Workflow File Location
The configuration for this workflow is stored in the `.github/workflows/build-app-javascript.yaml` file within the project repository.

### Workflow Triggers
This workflow is triggered by pushes to the repository. Specifically, it is triggered when changes occur in the `app_javascript` directory or in the workflow file itself.

### Jobs 
The CI workflow has three jobs:
- **Build Job:** Tests the code, installs dependencies, and lints the code using ESLint.
- **Security Job:** Ensures code security using Snyk by scanning for vulnerabilities.
- **Docker Job:** Builds and pushes a Docker image for the JavaScript application, but only if the previous jobs succeed.
