# Use a precise version of your base image
FROM python:3-alpine3.15

# Set the working directory
WORKDIR /app

# Copy only the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy only the application code into the container
COPY app.py .
COPY templates/index.html templates/

# Create a non-root user and switch to it
RUN adduser -D myuser
USER myuser

# Expose the port the app runs on
EXPOSE   5000

# Start the application
CMD ["python", "app.py"]
