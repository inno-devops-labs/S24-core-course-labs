// Import the express module
const express = require("express");
const env = require("dotenv");

env.config();
// Create an express application
const app = express();
const port = process.env.PORT ?? 5000;

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
