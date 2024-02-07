const express = require('express');
const moment = require('moment-timezone');

const app = express();

// Define a route for the homepage
app.get('/', (req, res) => {
    // Get the current time in Damascus timezone
    const damascusTime = moment.tz('Asia/Damascus').format('YYYY-MM-DD HH:mm:ss');
    // Send HTML response with the current time
    res.send(`<h1>The current time in Damascus, Syria:</h1><p>${damascusTime}</p>`);
});

// Start the server and listen on port 3000
const PORT = process.env.PORT || 3000;
const server = app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});

// Export the server instance to use in tests
module.exports = server;
