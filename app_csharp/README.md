# Time API

## Description

Simple Asp.net-based web API that can give you current time in Moscow Standard Time timezone.

## Local setup

### Setup

Get all dependencies and build the project:

```sh
dotnet build
```

### Launch

Then you can actually launch the app:

```sh
dotnet run --project Web --launch-profile https
```

### Interact

Now you can interact with the app. To see the current time in Moscow, visit <https://localhost:7273/time/msk>

## Interactive documentation

To view auto-generated Swagger docs, visit <https://localhost:7273/swagger>

## Docker

### Build

Run

```sh
docker build -t devops-cs .
```

### Pull

Run

```sh
docker pull dirakon/devops-cs:latest
```

### Run

Run (on host port 5000 as example)

```sh
docker run -p 5000:8080 dirakon/devops-cs:latest
```

## Unit tests

To run unit tests, do

```sh
dotnet test
```
