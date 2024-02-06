# Kotlin Web Application

A Web Application that displays current time in Moscow based on NTP Pool service (since the system may have incorrect time set)

## Installation and Running

```bash
./gradlew build # build
./gradlew run # run
./gradlew test # test
```

If everything goes well, you will see startup logs with message`Application - Responding at http://127.0.0.1:8000`. You can now see html page with moscow time at `localhost:8000`
