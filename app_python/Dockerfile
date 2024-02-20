# Use an official Python runtime as a parent image, specifying the exact version
FROM python:3.9.2-slim

# Set the working directory in the container
WORKDIR /app

# Use a non-root user for security purposes
RUN useradd -m myuser
USER myuser

# Copy only the necessary files
COPY --chown=myuser:myuser requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY --chown=myuser:myuser ./templates ./templates
COPY --chown=myuser:myuser app.py ./PYTHON.md ./README.md ./

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
