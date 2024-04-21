FROM eclipse-temurin:21.0.2_13-jdk-alpine AS build

WORKDIR /build

RUN adduser -D build && chown build:build /build

USER build

COPY --chown=build:build . /build

RUN ./gradlew build

FROM eclipse-temurin:21.0.2_13-jre-alpine

RUN adduser -DH app

WORKDIR /app

RUN mkdir /app/vol
RUN chown -R app:app /app

USER app

COPY --from=build /build/build/libs/devops_java-0.0.1-SNAPSHOT.jar /app/

RUN chmod 444 /app/devops_java-0.0.1-SNAPSHOT.jar

EXPOSE 8080

ENTRYPOINT ["java","-jar", "devops_java-0.0.1-SNAPSHOT.jar"]