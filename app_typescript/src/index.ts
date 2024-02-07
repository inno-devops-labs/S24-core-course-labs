import express from 'express';
import cors from 'cors';
import { DateTime } from 'luxon';

const app = express();
app.use(cors());
app.use(express.static('public'));

app.get('/api/time', (_req, res) => {
  const aktobeTime = DateTime.now().setZone('Asia/Dushanbe');
  const formattedTime = aktobeTime.toFormat("EEEE, dd LLLL yyyy 'at' HH:mm");
  res.send({ time: formattedTime });
});

const PORT = process.env.PORT ||  3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
