// app.js
// Importing the Express.js library
const express = require('express');
// Creating an instance of the Express application
const app = express();
// Importing the DateTime class from the Luxon library
const { DateTime } = require('luxon');

// Handling GET requests to the root endpoint '/'
app.get('/', (req, res) => {
    // Obtaining the current time in Moscow timezone and formatting it
    const moscowTime = DateTime.now().setZone('Europe/Moscow').toLocaleString(DateTime.DATETIME_FULL);
    // Sending a response with HTML content displaying the current time in Moscow
    res.send(`<h1>Current Time in Moscow:</h1><p>${moscowTime}</p>`);
});

// Defining the port for the server to listen on, using either the environment variable or defaulting to 3000
const PORT = process.env.PORT || 3000;
// Starting the server and logging its URL to the console
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
