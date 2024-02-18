# App Go

## Overview

This app starts server which provides page where you can add records to database and list all of them

## Development

### Requirements

- go 1.21 and higher
- optional: docker, docker compose, postgres database
- setup .env file

### Before developping

#### ENV

Put startup configuration in `.env` file

Example:
```
ENV=local

SERVER_HOST=0.0.0.0
SERVER_PORT=8080

DB_HOST=127.0.0.1
POSTGRES_USER=username
POSTGRES_PASSWORD=password
POSTGRES_DB=db
```

#### Postgres

Provide your postgres instance or use prepared one with `docker compose`

### Develop

#### Manual run

For running a server
```bash
make dev
```

For automigrations provided with `gorm`
```bash
make migrate
```

#### Docker

#### Pulling image

```bash
docker pull legolass322/devops:go-app
```

#### Building image

```bash
docker buildx b --build-arg runcmd=app_go -t devops:go-app .
docker buildx b --build-arg runcmd=migrate -t devops:go-migrate .
```

#### Running

```bash
docker run -p <PORT>:8080 devops:go-app
```

#### Docker compose

Will pull and build all needed images for application

Then will start the pg database, migrate, and serve

```bash
docker compose build
docker compose up
```