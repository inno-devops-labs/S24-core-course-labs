FROM eclipse-temurin:21-jdk-alpine AS base

RUN adduser app_java_user --system --shell=/bin/false
WORKDIR /app_java

ARG JAR_FILE
COPY --chown=app_java_user:app_java_user ${JAR_FILE} app.jar

USER app_java_user
EXPOSE 8000

CMD ["sh", "-c", "java -jar app.jar"]
