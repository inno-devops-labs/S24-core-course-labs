# Flutter Web Application

## Description

This is simple web application that displays the current time in Moscow. To develop the app, I used the Dart language and Flutter framework.

## Start

### Installation process

1. Clone the repository: `git clone https://github.com/Alyona-art/S24-core-course-labs.git`
1. Install [Dart and Flutter](https://docs.flutter.dev/get-started/install/)
1. Install all needed flutter packages `flutter pub get`

### Usage

Run the application using the following command

`flutter run -d chrome`

## Docker

### Build
```
docker build -t app-dart .
```

### Pull

```
docker pull alyonaart/app-dart:latest
```

### Run

```
docker run -d --name dart_container -p 8080:80 app-dart
```

The application will be accessible at http://127.0.0.1:8080