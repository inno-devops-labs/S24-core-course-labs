# World Clock Web Application

This simple web application built with NodeJS displays the current time in Moscow, Paris, London and New York City.

## Usage

1. Install dependencies using `npm install`.
2. Run the application using `npm start`.
3. Open your web browser and go to `http://127.0.0.1:3000/` to view the different timezones.

## Project Structure

- `app_nodejs/`: Main application folder.
  - `index.js`: NodeJS application code.
  - `views/`: EJS views.
  - `package.json`: NodeJS app description and dependencies.

## Docker

### Build the Docker Image

```bash
docker build -t node-world-clock-app .
```

### Pull the Docker Image

```bash
docker pull evsey/node-world-clock-app:latest
```

### Run the Docker Image

```bash
docker run -p 3000:3000 evsey/node-world-clock-app
```