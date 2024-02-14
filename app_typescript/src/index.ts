import express from 'express';
import cors from 'cors';
import { DateTime } from 'luxon';
import path from 'path';

const app = express();
app.use(cors());
app.use(express.static('public'));

app.get('/api/time', (_req, res) => {
  const aktobeTime = DateTime.now().setZone('Asia/Dushanbe');
  const formattedTime = aktobeTime.toFormat("EEEE, dd LLLL yyyy 'at' HH:mm");
  res.send({ time: formattedTime });
});

// Add this route handler to serve the index.html file
app.get('/', (_req, res) => {
  res.sendFile(path.join(__dirname, '../public/index.html'));
});

const PORT = process.env.PORT ||  3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
