FROM golang:1.21.5-alpine3.19

# Add labels for metadata
LABEL version="1.0" description="WebApp showing current Moscow time on golang" maintainer="rmolochko"

# Set up environment variables to ensure log output is not buffered
ENV GIN_MODE=release
ENV PORT=8081

# Set the working directory inside the container
WORKDIR /app

# Create a non-root user for running the application
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser && chown -R appuser /app

# Copy the go module files and download dependencies
COPY go.mod go.sum ./
RUN go mod download

# Copy the rest of the application code
COPY . .

# Build the application
RUN CGO_ENABLED=0 go build -o /moscow-time

# Create a logs directory and set its permissions
RUN mkdir /app/logs && mkdir /app/data && chown -R appuser:appuser /app

# Set the user to the non-root app user
USER appuser

# Expose the port on which the web server will run
EXPOSE 8081

# Command to run the executable
CMD ["/moscow-time"]
