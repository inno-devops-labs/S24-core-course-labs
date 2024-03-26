// Import the express and prom-client modules
const express = require("express");
const env = require("dotenv");
const client = require("prom-client");

// Load environment variables from .env file
env.config();

// Create an express application
const app = express();
const port = process.env.PORT || 5000; // Use 5000 if PORT is not provided in .env

// Create a new Prometheus collector
const collectDefaultMetrics = client.collectDefaultMetrics;

// Probe every 5th second.
collectDefaultMetrics({ timeout: 5000 });

// Expose metrics endpoint for Prometheus
app.get("/metrics", async (req, res) => {
  try {
    const metrics = await client.register.metrics();
    res.set("Content-Type", client.register.contentType);
    res.end(metrics);
  } catch (error) {
    console.error("Error generating metrics:", error);
    res.status(500).send("Internal Server Error");
  }
});

// Define route for homepage
app.get("/", (_, res) => {
  // Gets the current date and time in the specified time zone.
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
