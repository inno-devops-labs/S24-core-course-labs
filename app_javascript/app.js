const express = require('express');
const app = express();
const port = 3000;

module.exports = app;

app.set('view engine', 'ejs');
app.use(express.urlencoded({ extended: true }));

let todoList = [];

app.get('/', (req, res) => {
  res.render('index', { todoList });
});

app.post('/add', (req, res) => {
  const newTodo = req.body.todo;
  todoList.push(newTodo);
  res.redirect('/');
});

app.listen(port, () => {
  console.log(`Todo app listening at http://localhost:${port}`);
});
