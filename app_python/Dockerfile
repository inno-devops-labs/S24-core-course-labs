# Dockerfile

# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Create a non-root user
RUN useradd -m appuser

# Set the working directory to /app
WORKDIR /app

COPY requirements.txt app.py ./

COPY templates ./templates/

COPY static ./static/

# Change ownership to the non-root user
RUN chown -R appuser:appuser /app

# Switch to the non-root user
USER appuser

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install Flask
RUN pip install Flask

# Set the PATH to include the user's local bin directory
ENV PATH="/home/appuser/.local/bin:${PATH}"

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV FLASK_APP=app.py

# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
