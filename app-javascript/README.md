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
