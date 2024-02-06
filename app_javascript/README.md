# Moscow time app

## Description

A simple Express.js app that displays Moscow time.

## Getting started

1. Install `Express.js` framework:

```bash
npm install express
```

2. Run the application in the root folder:

```bash
node app.js
```

The application will start locally on port `3000`. You can access it by navigating to `http://127.0.0.1:3000` in the web browser.

## Endpoints

A single endpoint is currently present:

- `/` (GET): Returns an HTML page with the current Moscow time.

## Templates

Templates are stored in `views` folder.

- time.html - A simple html template with the large text in the center.

## Logging

The application writes the logs into console

## Error handling
If an error occurs, the app will log an error.
