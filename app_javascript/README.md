# JavaScript Web Application

This JavaScript web application displays the current time in Damascus, Syria.

## Installation

1. Clone this repository to your local machine

2. Navigate to the `app_javascript` directory:

    ```bash
    cd app_javascript
    ```

3. Install the required dependencies:

    ```bash
    npm install
    ```

## Usage

### Running the Application

1. Ensure you are in the `app_javascript` directory.

2. Start the application using the following command:

    ```bash
    node app.js
    ```

3. Open a web browser and navigate to `http://localhost:3000/` to view the page.
### Running the Tests

1. Ensure you are in the `app_javascript` directory.

2. Make sure the web page is not already running on the local host

3. Run the tests using the following command:

    ```bash
    npx mocha test.js
    ```

4. After running the command, you should see the output of the test results.

## Technologies Used

- Node.js
- Express.js
- moment-timezone
- Mocha
- Supertest