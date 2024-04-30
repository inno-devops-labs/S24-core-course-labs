# syntax=docker/dockerfile:1

# Use the official image as a parent image
FROM --platform=linux/arm64 python:3.10-alpine AS build

# Labelling the image
LABEL version="1.0" description="Flask Application showing current Moscow time" maintainer="rekhlov"

# Set the working directory
WORKDIR /app_python

# Create user
RUN adduser -D myuser && chown -R myuser /app_python
USER myuser

# Copy only the necessary files
COPY static ./static
COPY templates ./templates
COPY __init__.py app.py requirements.txt ./

# Install dependencies
RUN pip install -r requirements.txt --no-cache-dir --user

# Run the application
EXPOSE 5000
CMD [ "python", "-m", "flask", "run", "--host", "0.0.0.0", "--port", "5000"]