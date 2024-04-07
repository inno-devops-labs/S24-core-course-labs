# Use a base image with a precise version
FROM python:3-alpine3.15

# Set the working directory inside the container
WORKDIR /app

# Copy only the necessary files to the container
COPY app.py .
COPY requirements.txt .
COPY templates ./templates

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port on which the Flask application will listen
EXPOSE 5000

# Create a non-root user
RUN adduser -D myuser

# Set file ownership to the non-root user
RUN chown -R myuser:myuser /app

# Switch to the non-root user
USER myuser

# Set the command to run the application
CMD ["python", "app.py"]