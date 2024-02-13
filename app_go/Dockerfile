# Start from the latest golang base image
FROM golang:1.21.3-alpine

# Set environment variables
ENV APP_HOME /app_go

# Set the Current Working Directory inside the container
WORKDIR $APP_HOME

# Copy go mod and sum files
COPY go.mod go.sum main.go $APP_HOME/
COPY templates/ $APP_HOME/templates/

# Create a non-root user and remove write permissions for the group and others
RUN adduser --disabled-password appuser && chmod -R a-w+x+r $APP_HOME

# Download all dependencies. Dependencies will be cached if the go.mod and go.sum files are not changed
RUN go mod download && go build -o main .

# Switch to the non-root user
USER appuser

# Expose port 8080 to the outside world
EXPOSE 8080

# Command to run the executable
CMD ["./main"]