# Moscow Time Web Application

This is a simple web application that shows the current time in Moscow.

## Getting started locally

### Prerequisites

- .NET 7 SDK

### Usage

```bash
cd MoscowTime
dotnet run
```

The running app will be available at http://localhost:5196

## Getting started with Docker

### Prerequisites

- Docker

### Usage

Build the image:

```bash
docker build -t majorro/devops-engineering-course:dotnet MoscowTime
```

or pull it from Docker Hub:

```bash
docker pull majorro/devops-engineering-course:dotnet
```

Run the container:

```bash
docker run -p 5196:80 majorro/devops-engineering-course:dotnet
```

The running app will be available at http://localhost:5196

## Contact

- [Telegram](https://t.me/majorro228)
