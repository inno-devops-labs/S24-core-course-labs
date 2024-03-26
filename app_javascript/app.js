const express = require('express');
const app = express();
const promClient = require('prom-client')
const port = 5001;

module.exports = app;

// Set the view engine to EJS
app.set('view engine', 'ejs');

app.use(express.urlencoded({ extended: true }));

// Array to store todo items
let todoList = [];

// Route handler for the home page
app.get('/', (req, res) => {
  res.render('index', { todoList });
});

// Route handler to add a new todo item
app.post('/add', (req, res) => {
  const newTodo = req.body.todo;
  todoList.push(newTodo);
  res.redirect('/');
});

// Route handler for Prometheus metrics
app.get('/metrics', async (req, res) => {
  res.set('Content-Type', promClient.register.contentType);
  res.send(await promClient.register.metrics());
});

// Initialize default metrics
promClient.collectDefaultMetrics();

// Start the server and listen for incoming requests
app.listen(port, () => {
  console.log(`Todo app listening at http://localhost:${port}`);
});