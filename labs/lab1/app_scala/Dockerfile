FROM sbtscala/scala-sbt:eclipse-temurin-focal-17.0.10_7_1.9.8_3.3.1 AS builder

WORKDIR /app

COPY build.sbt .
COPY project/ project/
COPY src/ src/

RUN sbt missinglinkCheck compile test assembly

FROM eclipse-temurin:17.0.10_7-jre-jammy

ARG USER_NAME=appuser
ARG GROUP_NAME=appgroup

RUN groupadd $GROUP_NAME \
  && useradd -g $GROUP_NAME $USER_NAME

USER $USER_NAME

WORKDIR /app

COPY --from=builder /app/target/scala-3.3.1/moscowTime.jar /app/moscowTime.jar

ENTRYPOINT ["java", "-jar", "moscowTime.jar"]
