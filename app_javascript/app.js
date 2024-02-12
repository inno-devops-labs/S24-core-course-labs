const express = require('express');
const app = express();
const port = 3000;

const ejs = require('ejs');

const path = require('path');
const isPkg = typeof process.pkg !== 'undefined';
const basePath = isPkg ? path.join(path.dirname(process.execPath)) : __dirname;

app.set('views', path.join(basePath, 'views'));
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

process.on('SIGINT', function() {
    console.log("\nGracefully shutting down from SIGINT (Ctrl+C)");
    process.exit();
});
