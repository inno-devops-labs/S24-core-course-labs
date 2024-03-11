const express = require('express');
const app = express();
const port = 3001;

app.set('view engine', 'ejs');

app.get('/', (req, res) => {
    const timeData = getTimeData();
    res.render('index', { timeData });
});

function getTimeData() {
    const cities = ['Moscow', 'Paris', 'London', 'New York City'];
    const timeData = {};

    cities.forEach(city => {
        const timezone = getTimezone(city);
        const time = new Date().toLocaleString('en-US', { timeZone: timezone });
        timeData[city] = time;
    });

    return timeData;
}

function getTimezone(city) {
    switch (city) {
        case 'Moscow':
            return 'Europe/Moscow';
        case 'Paris':
            return 'Europe/Paris';
        case 'London':
            return 'Europe/London';
        case 'New York City':
            return 'America/New_York';
        default:
            return 'UTC';
    }
}

app.listen(port, () => {
    console.log(`Server is running at http://localhost:${port}`);
});
