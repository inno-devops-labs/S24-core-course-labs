// Server-side JavaScript code (for Node.js)
const express = require('express');
const app = express();
const port = 3000;

app.get('/', (req, res) => {
  const now = new Date().toLocaleString("ru-RU", {
    timeZone: "Europe/Moscow",
  });
  res.send(`Time in Moscow : ${now}`);
});

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});