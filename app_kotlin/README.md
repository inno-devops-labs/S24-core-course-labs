## Kotlin web app

This is simple kotlin Spring Boot application for obtaining current time in Europe/Moscow timezone

Install dependencies and build project:
```bash
./gradlew build
```
Start server:
```bash
./gradlew bootrun
```
This will start a local web server, and you can access the current time in Moscow by going to http://127.0.0.1:8080/ in your web browser.

Example result:
```The current time in Moscow is 15:40:22```


Additionaly you can run unittests by command:
```bash
./gradlew test
```