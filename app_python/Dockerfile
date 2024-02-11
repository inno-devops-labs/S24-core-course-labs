# Use the official Python base image
FROM python:3.9-slim

# Set working directory for container
WORKDIR /app

# Copy file with project requirements
COPY requirements.txt .

# Upgrade pip and install python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Make directory to start app as module
RUN mkdir "app_python"

# Copy all necessary files
COPY . .

# Create non-root user
RUN useradd -m user

# Run app as non-root user
USER user

EXPOSE 8080 8080

# Run the application
ENTRYPOINT ["python3", "-m", "src"]