# Node.js Express Web Application Documentation

This documentation provides a comprehensive guide to the Node.js web application developed using the Express framework.

## Overview

The web application's primary functionality is to display the current time in Moscow. Leveraging the power of Express, it establishes a straightforward web server in Node.js and utilizes Luxon's DateTime class to fetch and format the present time.

## Code Structure

The application consists of a single JavaScript file:

- `app.js`: This file encapsulates the core logic for the Express web application. It orchestrates the import of essential modules, creates an instance of the Express application, and establishes a route to handle requests to the root URL (/). Upon receiving a request at this route, a callback function executes, fetching the current time in Moscow and responding accordingly.

## Implementation Details

### Express Application Initialization

- The Express web application is initialized by importing the `express` module and creating an Express application instance using `express()`.

```javascript
const express = require("express");
const app = express();
```

### Define Route for Homepage

- The route `/` is defined using `app.get('/')`. This method specifies a callback function to be executed when a GET request is made to the root URL.

```javascript
app.get("/", (req, res) => {
  // code
});
```

### Current Time Retrieval

- Within the route handler function, the application leverages Luxon's DateTime class to fetch the current time in Moscow and format it.

```javascript
const moscowTime = DateTime.now()
  .setZone("Europe/Moscow")
  .toLocaleString(DateTime.DATETIME_FULL);
```

### Sending Response

- The retrieved current time in Moscow is sent as a response to the client using `res.send()`.

```javascript
res.send(`<h1>Current Time in Moscow:</h1><p>${moscowTime}</p>`);
```

### Running the Express Application

- The Express application launches and listens on port 3000, with the option to use the environment variable for dynamic port assignment.

```javascript
const PORT = process.env.PORT || 3000;
// Starting the server and logging its URL to the console
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
```

### Docker

#### Containerized Application

The application is containerized using Docker, ensuring portability and ease of deployment across different environments. Below are instructions for building, pulling, and running the Docker container.

#### How to Build

To build the Docker image locally, follow these steps:

```bash
docker build -t mtz_js .
```

This command builds the Docker image based on the provided Dockerfile (`Dockerfile`) in the `app_javascript` directory and tags it with the name `mtz_js`.

#### How to Pull

If you prefer to pull the pre-built Docker image from a container registry instead of building it locally, you can use the following command:

```bash
docker pull wesamnaseer/mtz_js
```

#### How to Run

Once you have either built the Docker image locally or pulled it from a registry, you can run the container using the following command:

```bash
docker run -p 3000:3000 -e PORT=3000 wesamnaseer/mtz_js
```

#### Testing Current Time Formatting

- We have a unit test named `app.test.js` which verifies that the current time retrieved by our application is correctly formatted in the expected format.

#### Running the Unit Tests

To run the unit tests for the JavaScript application, follow these steps:

1. **Navigate to the Application Directory:**

   - Open a terminal or command prompt.
   - Navigate to the directory where your JavaScript application (`app_javascript`) is located.

2. **Install Testing Dependencies (if not already installed):**

   - Ensure that the required testing dependencies are installed. You can install them using npm:

     ```
     npm install
     ```

3. **Run the Unit Tests:**

   - Run the following command to execute the unit tests:

     ```
     npm run test
     ```

   - This command will execute the tests defined in the `app.test.js` file within the `tests` directory.

4. **View Test Results:**

   - After running the tests, the test runner (such as Jest) will display the test results in the terminal. You should see information about the test cases executed and whether they passed or failed.
