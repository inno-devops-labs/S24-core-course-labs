# Use the official Python image as the base image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN apt-get update \
    && apt-get install -y gcc \
    && pip install --upgrade pip \
    && pip install Flask gunicorn pytz \
    && pip install prometheus_client

# Set the working directory
WORKDIR /app

# Copy application files
COPY . /app

# Expose port 5000
EXPOSE 5000

# Define the startup command
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
