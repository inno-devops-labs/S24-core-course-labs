// Server-side JavaScript code (for Node.js)
const express = require('express');
const env = require("dotenv");
const fs = require("fs");

env.config();

const app = express();
const port = 3000;


let visitCount = 0;
const VISIT_FILE = "visits.txt";

const readVisitCountFromFile = () => {
  try {
    const count = fs.readFileSync(VISIT_FILE, "utf-8");
    return parseInt(count);
  } catch (err) {
    // If the file doesn't exist or cannot be read, create a new file with 0 visits
    return 0;
  }
};

visitCount = readVisitCountFromFile();

app.use((req, res, next) => {
  visitCount++;
  fs.writeFileSync(VISIT_FILE, visitCount.toString());
  next();
});

app.get('/', (req, res) => {
  const now = new Date().toLocaleString("ru-RU", {
    timeZone: "Europe/Moscow",
  });
  res.send(`Time in Moscow : ${now}`);
});

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});

app.get("/visits", (_, res) => {
  const visits = fs.readFileSync(VISIT_FILE, "utf-8");
  res.send(`Total visits: ${visits}`);
});