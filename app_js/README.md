# JavaScript Web Application

This repository contains a simple web application developed using JavaScript.

## Overview

The web application displays a basic greeting message using JavaScript.

## Installation

1. Clone the repository to your local machine:

2. Navigate to the `app_js` directory:

3. Open the `index.html` file in a web browser to view the application.

## Docker

### Containerized Deployment

Our JavaScript web application can be easily deployed using Docker, ensuring consistency and portability across different environments.

### How to Use Docker

#### Building the Docker Image

To build the Docker image locally, follow these steps:

1. Make sure you have Docker installed on your machine.
2. Navigate to the `app_js` folder in your terminal.
3. Run the following command to build the Docker image:
   ```bash
   docker build -t my-js-app .
   docker run -d -p 8080:80 --name my-js-container my-js-app
   ```

## Usage

- Open the `index.html` file in any modern web browser.
- You will see a greeting message displayed on the screen.

## Dependencies

This web application does not require any external dependencies or libraries.

## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvement, please open an issue or create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

