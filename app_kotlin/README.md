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

Moreover, on http://127.0.0.1:8080/visits in your web browser you can get number of visits of site

Example result:
```{visits: 9}```


Additionaly you can run unittests by command:
```bash
./gradlew test
```

### Running with docker

You may use already built image:

```bash
docker pull pgrammer/app_kotlin
docker run -p 8080:8080 pgrammer/app_kotlin
```

Or build it yourself:

```bash
docker build -t app_kotlin .
docker run -p 8080:8080 app_kotlin
```

Now you can see Moscow time at http://localhost:8080