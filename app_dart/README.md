# Flutter Web Application

[![Dart CI](https://github.com/Alyona-art/S24-core-course-labs/actions/workflows/app_dart.yml/badge.svg)](https://github.com/Alyona-art/S24-core-course-labs/actions/workflows/app_dart.yml)

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

## Unit Tests

Run the tests using the following command

```
flutter test --platform chrome test/time_test.dart
```

## Visits counter

I implemented persistence logic in this app: visits are counted and tracked in the Firestore collection