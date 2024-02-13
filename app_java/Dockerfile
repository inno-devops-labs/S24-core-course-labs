FROM maven:3.8.4-openjdk-17-slim AS build

WORKDIR /app

COPY pom.xml ./
COPY src ./src

RUN mvn package

FROM openjdk:17

WORKDIR /app

COPY --from=build  /app/target/spring-boot-docker.jar ./

RUN adduser app_user

RUN rm /bin/sh /bin/bash

USER app_user:app_user

ENTRYPOINT ["java", "-jar", "spring-boot-docker.jar"]