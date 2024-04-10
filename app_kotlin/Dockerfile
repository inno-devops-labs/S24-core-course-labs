FROM gradle:8.6-jdk17-alpine AS build

WORKDIR /home/gradle/src

COPY --chown=gradle:gradle src /home/gradle/src/src
COPY --chown=gradle:gradle build.gradle.kts /home/gradle/src
COPY --chown=gradle:gradle gradle.properties /home/gradle/src

RUN gradle buildFatJar --no-daemon


FROM eclipse-temurin:17-jdk-alpine

WORKDIR /app

ENV VISITS_FILE="visits.txt"
ENV VISITS_PATH="/app/visits"

RUN mkdir $VISITS_PATH
RUN addgroup -S group && adduser -S user -G group
RUN chgrp -R group /app && chmod g+rw -R /app

USER user

COPY --from=build /home/gradle/src/build/libs/*.jar ./app.jar

EXPOSE 8000

ENTRYPOINT ["java","-jar","/app/app.jar"]
