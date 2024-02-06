const express = require('express');
const app = express();
const port = 3000;
const path = require('path');

const ejs = require('ejs');

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.engine('html', ejs.renderFile);
app.set('view engine', 'html');

app.get('/', (req, res) => {
    try {
        let moscowTime = new Date().toLocaleString("en-US", { timeZone: "Europe/Moscow" });
        res.render('time', { time: moscowTime });
        console.log(`Showed time: ${moscowTime}`);
    }
    catch (e) {
        res.status(500).send("Failed to show time. Soryan.");
        console.error("Failed to show time. Error: ", e);
    }
});

app.listen(port, function () {
    console.log(`Server is running on port ${port}`);
});
