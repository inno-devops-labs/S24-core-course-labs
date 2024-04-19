FROM openjdk:23-bookworm AS base

ARG UID=10001
ARG GID=10001

RUN groupadd -g "${GID}" user \
    && useradd -u "${UID}" -g "${GID}" user
WORKDIR /app_java

ARG JAR_FILE
COPY --chown=user:user ${JAR_FILE} app.jar

RUN mkdir -p ./app/data/
RUN chown -R user ./app

USER user
EXPOSE 8080

ENV SPRINGPROFILES=prod,actuator

CMD ["sh", "-c", "java -Dspring.profiles.active=${SPRINGPROFILES} -jar app.jar"]
