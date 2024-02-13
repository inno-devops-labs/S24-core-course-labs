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
5. Running tests: 
   ```bash
   npm test
   ``` 

## Docker 

### Building the Docker Image (Locally)

1. **Building the image**
   ```bash 
   docker build -t app_javascript .
   ```
2. **Running the container at [localhost:3000](127.0.0.1/3000)**
   ```bash 
   docker run -d -p 3000:3000 --name app_javascript_container app_javascript
   ```

### Building the Docker Image (Docker Hub)

1. **Building the image**
   ```bash 
   docker pull cogbonna/app_javascript_image
   ```
2. **Running the container at [localhost:3000](127.0.0.1/3000)**
   ```bash 
   docker run -dp 0.0.0.0:3000:3000 cogbonna/app_javascript_image
   ```