FROM sbtscala/scala-sbt:eclipse-temurin-focal-17.0.10_7_1.9.8_3.3.1

WORKDIR /app

COPY . .

RUN sbt test

CMD ["sbt", "run"]
