# Using the Python Alpine image as the base image
FROM python:3.9.18-alpine3.19@sha256:7e53de21917d6793787bc67483838360404bb2fd70d9c3e38ccc243790c323b2

# Set the working directory in the container
WORKDIR /app

# Add a new non-root user
RUN adduser -D myuser && mkdir /app/app_python && chown -R myuser ./app_python
USER myuser

# Copy requirements.txt 
COPY requirements.txt ./app_python/requirements.txt

# Install dependencies
RUN pip install -r ./app_python/requirements.txt --no-cache-dir --user

# Copy relevant folders 
COPY app ./app
COPY tests ./tests
COPY static ./static

# Expose port 5000
EXPOSE 5000

LABEL maintainer="c.ogbonna@innopolis.university"
LABEL description="Docker image for Flask app."

# Run the app
CMD ["python3", "app/routes.py"]