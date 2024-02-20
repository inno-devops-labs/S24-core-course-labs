# Stage 1: Build the application
FROM maven:3.8.4 AS build
WORKDIR /app
COPY . .
RUN mvn clean package

# Stage 2: Create the final image
FROM openjdk:17-jdk-slim
RUN adduser springuser
WORKDIR /app
COPY --from=build /app/target/app_java-0.0.1-SNAPSHOT-jar-with-dependencies.jar /app/
EXPOSE 8080
CMD ["java", "-jar", "app_java-0.0.1-SNAPSHOT-jar-with-dependencies.jar"]
COPY .dockerignore /app/.dockerignore
RUN chown -R springuser:springuser /app
USER springuser