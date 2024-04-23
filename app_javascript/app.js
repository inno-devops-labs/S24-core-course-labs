// Import the express module
const express = require("express");
const env = require("dotenv");
const fs = require("fs");

env.config();
// Create an express application
const app = express();
const port = process.env.PORT ?? 5000;

let visitCount = 0;

const VISIT_FILE = "visits.txt";
// Function to read visit count from file
const readVisitCountFromFile = () => {
  try {
    const count = fs.readFileSync(VISIT_FILE, "utf-8");
    return parseInt(count);
  } catch (err) {
    // If the file doesn't exist or cannot be read, create a new file with 0 visits
    return 0;
  }
};

// Read visit count from file when the application starts
visitCount = readVisitCountFromFile();

// Middleware to increment visit count on each request
app.use((req, res, next) => {
  visitCount++;
  fs.writeFileSync(VISIT_FILE, visitCount.toString());
  next();
});

// Endpoint to display the recorded visits
app.get("/visits", (_, res) => {
  const visits = fs.readFileSync(VISIT_FILE, "utf-8");
  res.send(`Total visits: ${visits}`);
});

app.get("/", (_, res) => {
  /**
   * Gets the current date and time in the specified time zone.
   * @returns {string} The current date and time in the format "dd/mm/yyyy, hh:mm:ss".
   */
  const now = new Date().toLocaleString("ru-RU", {
    timeZone: "Europe/Moscow",
  });
  res.send(`The current time in Moscow is: ${now}`);
});

// Start the server only if the file is executed directly
if (require.main === module) {
  app.listen(port, () => {
    console.log(`Server is running on http://localhost:${port}`);
  });
}

module.exports = app;
