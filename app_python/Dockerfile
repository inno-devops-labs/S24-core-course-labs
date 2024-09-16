# Use a specific Python version as the base image
FROM python:3.9.18-bullseye AS base

# Create a non-root user
RUN adduser --system --group appuser

# Switch to the non-root user
USER appuser

# Set the working directory and assign ownership to the non-root user
WORKDIR /app
RUN chown -R appuser:appuser /app

# Copy only the requirements file to avoid unnecessary files in the build context
COPY --chown=appuser:appuser requirements.txt .

# Install the required packages as the non-root user
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install --no-cache-dir -r requirements.txt

# Copy the application files
COPY --chown=appuser:appuser app.py .

# Set a build argument for the port
ARG PORT=5000

# Expose the port
EXPOSE $PORT

# Setup the build 
# Specify the command to run the Flask application
CMD ["python", "app.py"]