# Use an official Python runtime as a parent image
FROM python:3.9.18-alpine3.19
# Set non-root user and group IDs
ARG USER_ID=1000
ARG GROUP_ID=1000

# Create a non-root user and group
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser

# Set the working directory in the container
WORKDIR /python_app

# Copy only the necessary files into the container
COPY app.py DOCKER.md PYTHON.md README.md ./
COPY template/* ./template
# Set a non-root user

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt && rm -rf /root/.cache

# Change the ownership of the application directory to the non-root user
RUN chown -R appuser:appgroup /python_app

USER appuser

# Make port 80 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python3", "app.py"]

