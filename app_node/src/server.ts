import express from 'express';
import moment from 'moment-timezone';

const app = express();
const port = 3000;

app.get('/currentTime', (req, res) => {
  const currentTime = moment().tz('Europe/Moscow').format('YYYY-MM-DD HH:mm:ss');
  res.send({ currentTime });
});

const server = app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

export default server;
