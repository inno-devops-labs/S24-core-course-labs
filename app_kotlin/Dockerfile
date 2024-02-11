FROM openjdk:17-jdk-slim as builder

ARG USER_NAME=myuser

EXPOSE 8080
WORKDIR /app
COPY src/ /app/src/
COPY gradle/ /app/gradle/
COPY gradlew build.gradle /app/
# Create user and set ownership and permissions as required
RUN adduser $USER_NAME && chown -R $USER_NAME /app
# ... copy application files
USER $USER_NAME
RUN ./gradlew bootjar

FROM openjdk:17-jdk-slim
COPY --from=builder /app/build/libs/app-0.0.1.jar /app.jar
CMD ["java", "-jar", "app.jar"]