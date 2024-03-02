# Java Sample Application

## Overview

This is a simple java web application that shows current time in **Samara**.

## Installation

- Clone this repository and navigate to the project directory:

```bash
git clone https://github.com/dmfrpro/S24-core-course-labs -b lab1
cd S24-core-course-labs/app_java
```

- Install [maven](https://www.baeldung.com/install-maven-on-windows-linux-mac)

- Run the application and test:

```bash
mvn install
curl localhost:8080
```

## Docker

### Build

```bash
cd S24-core-course-labs/app_java
mvn clean compile assembly:single
docker build --build-arg \
    JAR_FILE=target/app-0.0.1-SNAPSHOT-jar-with-dependencies.jar \
    --tag=dmfrpro/app_java:v1.0 .
```

### Pull and Run

```bash
docker pull dmfrpro/app_java:v1.0
docker run -p 8080:8080 dmfrpro/app_java:v1.0
```
