# Moscow Time Display Web Application (JavaScript version)

## Overview

This JavaScript web application uses Express.js to display the current time in Moscow. It provides a simple and lightweight solution for users interested in real-time Moscow time.

## Features

- Display of current time in Moscow.
- Built with Express.js, a web framework for Node.js.
- Follows best practices and coding standards.

## Best Practices

1. **Code Comments:** The code has comments to explain important parts, like how it gets the current date and time in the chosen timezone.

2. **Code Quality:** The code is straightforward, focusing on showing the current time in Moscow. Adding a few more comments or documentation could make it even easier to understand and maintain..

## How To Install and Test

To run the Node.js Express web application, follow these steps:

2. **Install Dependencies:**

   - Make sure you have Node.js installed on your system.
   - Install the required dependencies by running:
     ```
     npm install
     ```

3. **Run the Application:**

   - After installing dependencies, navigate to the directory containing the `app.js` file.
   - Run the following command to start the Express server:
     ```
     node app.js
     ```

### Unit Test: Testing Current Time Format

#### Purpose:

- The `test_current_time_format` unit test ensures that the Express application endpoint `/` returns the current time in Moscow with the expected format `DD.MM.YYYY, HH:MM.SS`.

#### Test Setup:

- The test suite utilizes the `supertest` library to perform HTTP requests to the Express application.
- The Express application instance is imported from the `app.js` file to enable testing.

```javascript
const request = require("supertest");
const app = require("../app");
```

#### Test Function:

- The `GET /` test case sends a GET request to the `/` endpoint and verifies that the response contains the current time in the specified format.

```javascript
describe("GET /", () => {
  it("should return the current time in Moscow", async () => {
    const response = await request(app).get("/");
    expect(response.status).toBe(200);
    expect(response.text).toMatch(
      /The current time in Moscow is: \d{2}.\d{2}.\d{4}, \d{2}:\d{2}.\d{2}/gm
    );
  });
});
```

#### Best Practices Applied:

- **Asynchronous Testing**: Uses `async` and `await` to handle asynchronous operations, ensuring proper sequencing and error handling in test execution.
- **Assertion**: Asserts the expected behavior of the Express application, validating both the HTTP status code and the format of the response text.
- **Regular Expressions**: Employs a regular expression to verify that the response contains the current time in the expected format, enabling precise validation.
- **Separation of Concerns**: Defines the test case within a separate `describe` block, enhancing readability and organization of test suites.
