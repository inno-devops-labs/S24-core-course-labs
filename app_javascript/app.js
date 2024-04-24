const express = require('express');
const app = express();
const port = 3000;

const ejs = require('ejs');

const path = require('path');
const isPkg = typeof process.pkg !== 'undefined';
const basePath = isPkg ? path.join(path.dirname(process.execPath)) : __dirname;

const promBundle = require('express-prom-bundle');
const metricsMiddleware = promBundle({ includeMethod: true, includePath: true });
const fs = require('fs');

const dirPath = path.join(__dirname, 'visits');

if (!fs.existsSync(dirPath)) {
    fs.mkdirSync(dirPath, { recursive: true });
}

const filePath = path.join(dirPath, 'visits');

if (!fs.existsSync(filePath)) {
    fs.writeFileSync(filePath, '0');
}

app.use(metricsMiddleware);

app.set('views', path.join(basePath, 'views'));
app.engine('html', ejs.renderFile);
app.set('view engine', 'html');

app.get('/', (req, res) => {
    try {
        let moscowTime = new Date().toLocaleString("en-US", { timeZone: "Europe/Moscow" });
        res.render('time', { time: moscowTime });
        console.log(`Showed time: ${moscowTime}`);
        
        let visits = parseInt(fs.readFileSync(filePath, 'utf8'));
        fs.writeFileSync(filePath, (visits + 1).toString());

    }
    catch (e) {
        res.status(500).send("Failed to show time. Soryan.");
        console.error("Failed to show time. Error: ", e);
    }
});

app.get('/visits', (req, res) => {
    try {
        let visits = parseInt(fs.readFileSync(filePath, 'utf8'));
        res.send(`Number of visits: ${visits}`);
        console.log(`Number of visits: ${visits}`);
    }
    catch (e) {
        res.status(500).send("Failed to show number of visits. Soryan.");
        console.error("Failed to show number of visits. Error: ", e);
    }
});

app.get('/metrics', metricsMiddleware);

const server = app.listen(port, function () {
    console.log(`Server is running on port ${port}`);
});

process.on('SIGINT', function() {
    console.log("\nGracefully shutting down from SIGINT (Ctrl+C)");
    process.exit();
});

module.exports = { app, server };
