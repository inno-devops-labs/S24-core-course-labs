# TypeScript Web Application

## Overview
This application serves the current time in my hometown Aktobe,Kazakhstan using Node.js and TypeScript.

## Features
- Real-time display of Aktobe time.
- Responsive client-side updates.

## Installation
1. Clone the repository: `git clone https://github.com/a1kuat/S24-core-course-labs.git`
2. Change into the project directory: `cd app_typescript`
3. Install dependencies: `npm install`
4. Build the project: `npm run build`
5. Start the application: `npm run start`

## Usage
Open a web browser and navigate to `http://localhost:3000` to view the current time in Aktobe.

## Building the Docker Image

To build the Docker image, navigate to the directory containing the `Dockerfile` and run:

`bash docker build -t my-typescript-app . `

## Pulling the Docker Image

The image is pushed to my Docker Hub, you can pull it using:

`bash docker pull a1kuat/my-typescript-app`

## Running the Docker Image

To run the Docker image locally, use:

`bash docker run -p 3000:3000 -d my-typescript-app`


Then visit `http://localhost:3000/` in your web browser to see the application in action.