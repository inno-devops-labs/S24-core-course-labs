# Node.js Express Web Application Documentation

This documentation provides an overview of the Node.js web application built using Express.

## Overview

The web application displays the current time in Moscow. It utilizes the Express framework to create a simple web server in Node.js and the `toLocaleString` method to retrieve and format the current time.

## Code Structure

The application consists of a single JavaScript file:

- `app.js`: This file contains the main code for the Express web application. It imports the necessary modules, creates an Express application instance, and sets up a route to handle requests to the root URL (`/`). When a request is received at this route, the callback function is called to retrieve the current time in Moscow and return it as a response.

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
  // Function implementation goes here
});
```

### Current Time Retrieval

- Inside the route handler function, the current time in Moscow is retrieved using the `toLocaleString` method with the Russian locale and the Europe/Moscow timezone.

```javascript
const now = new Date().toLocaleString("ru-RU", { timeZone: "Europe/Moscow" });
```

### Sending Response

- The retrieved current time in Moscow is sent as a response to the client using `res.send()`.

```javascript
res.send(`The current time in Moscow is: ${now}`);
```

### Running the Express Application

- The Express application is started and listens on port 5000 using the `app.listen()` method.

```javascript
const port = 5000;
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
```

## How To Install and Test

To run the Node.js Express web application, follow these steps:

1. **Install Node.js:**

   - Make sure you have Node.js installed on your system.

2. **Install Dependencies:**

   - Navigate to the directory containing the `app.js` file.
   - Install the required dependencies by running:
     ```
     npm install
     ```

3. **Run the Application:**

   - After installing dependencies, run the following command to start the Express server:
     ```
     node app.js
     ```

4. **Test:**

   - Open a web browser and visit `http://localhost:5000/` to access the application.
   - You should see the current time in Moscow displayed on the webpage.
   - Refresh the browser tab to ensure the application continues to work as expected.

   ![Website screen](./screenshots/test.png)
   ![Terminal screenshot](./screenshots/terminal.png)
