# Use an official Python runtime as a parent image
FROM python:3.9.18-alpine3.19@sha256:7e53de21917d6793787bc67483838360404bb2fd70d9c3e38ccc243790c323b2

# Set the working directory in the container
WORKDIR /app

# Install build tools
RUN apk update && \
    apk add --no-cache build-base

# Copy only necessary files into the container and install dependencies
COPY . ./

# Install required libraries
RUN pip install --no-cache-dir -r requirements.txt

# Give ownership only for non-executable items
RUN addgroup -S flask && \
    adduser -S flask -G flask && \
    chown -R flask:flask /app/templates

# Grant read and write permissions to the 'visits' file
RUN chmod +rw /app/files/visits

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run the application as a non-root user
USER flask:flask

# Run app.py when the container launches
ENTRYPOINT ["flask", "run", "--host=0.0.0.0"]
