# Using the Python Alpine image as the base image
FROM python:alpine3.19@sha256:849ed6079c9f797ca9c1b7d6aea1c00aea3ac35110cbd0d6003f15950017ea8d

# Set the working directory in the container
WORKDIR /app

# Add a new non-root user
RUN adduser -D myuser && mkdir /app/app_python && chown -R myuser ./app_python
USER myuser

# Copy requirements.txt 
COPY requirements.txt ./app_python/requirements.txt

# Install dependencies
RUN pip install -r ./app_python/requirements.txt --no-cache-dir --user

# Copy the rest of the application
COPY . .

# Expose port 5000
EXPOSE 5000

LABEL maintainer="c.ogbonna@innopolis.university"
LABEL description="Docker image for Flask app."

# Run the app
CMD ["python3", "app/routes.py"]