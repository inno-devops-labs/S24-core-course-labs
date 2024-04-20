# Use a precise version of the base image
FROM python:3-alpine3.15

# Set the working directory in the container
WORKDIR /app

# Copy only specific files
COPY src/moscow_time/app.py requirements.txt config.py /app/

# Install virtualenv
RUN python -m venv /opt/venv

# Set environment variables for virtualenv
ENV PATH="/opt/venv/bin:$PATH" \
    VIRTUAL_ENV="/opt/venv"

# Install any needed dependencies specified in requirements.txt within the virtual environment
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Create a non-root user and group
RUN addgroup -S flaskgroup && adduser -S flaskuser -G flaskgroup

# Change ownership of the working directory to the non-root user
RUN chown -R flaskuser:flaskgroup /app

# Switch to the non-root user
USER flaskuser

# Define environment variable
ENV FLASK_APP=app.py

# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0"]
