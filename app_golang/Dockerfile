# Use a multi-stage build to keep the final image small
# Start with a builder image
FROM golang:1.18-alpine AS builder

# Set the working directory
WORKDIR /app

# Copy the go mod and sum files to download dependencies
COPY go.mod ./
RUN go mod download

# Copy the rest of the source code
COPY . .

# Build the application
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o msktime .

# Use a small base image
FROM alpine:latest

# Install tzdata for time zone information
RUN apk add --no-cache tzdata

# Set a non-root user
RUN adduser -D user
USER user

# Set the working directory in the container
WORKDIR /app

# Copy the binary from the builder stage
COPY --from=builder /app/msktime .

# Expose the port the app listens on
EXPOSE 8080

# Command to run the executable
CMD ["./msktime"]
