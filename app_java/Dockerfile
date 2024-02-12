
# Use a base image with Java installed
FROM adoptopenjdk/openjdk11:alpine-jre3.15

# Create a non-root user
RUN adduser -D springuser

# Set the working directory in the container
WORKDIR /app

# Copy only the necessary files into the container
COPY target/your-spring-application.jar /app/

# Expose the port that the Spring Boot application will run on
EXPOSE 8080

# Specify the command to run the Spring Boot application when the container starts
CMD ["java", "-jar", "your-spring-application.jar"]

# Use .dockerignore to exclude unnecessary files from being copied into the container
COPY .dockerignore /app/.dockerignore

# Change ownership of the application directory to the non-root user
RUN chown -R springuser:springuser /app

# Switch to the non-root user
USER springuser