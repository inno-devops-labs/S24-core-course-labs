# Use a precise version of the base image and language
FROM python:3.9-slim

# Create a non-root user and set permissions
RUN useradd appuser \
    && mkdir /app \
    && chown -R appuser /app

# Set the working directory in the container
WORKDIR /app

# Copy only necessary files
COPY --chown=appuser:appuser requirements.txt app.py /app/

# Create the templates directory and copy its contents
RUN mkdir /app/app_templates && \
    chown -R appuser /app/app_templates
COPY --chown=appuser:appuser app_templates/ /app/app_templates/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

RUN mkdir /app/data

# Run app.py when the container launches
CMD ["python", "app.py"]
