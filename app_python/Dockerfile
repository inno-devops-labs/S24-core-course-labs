# Use the official lightweight Python image
FROM python:3.11-slim

# Set a working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .

# Install dependencies in a virtual environment for security and isolation
RUN python -m venv /opt/venv && \
    . /opt/venv/bin/activate && \
    pip install --no-cache-dir -r requirements.txt

# Add application code to the container
COPY . .

# Expose port 5000 for Flask
EXPOSE 5000

# Set environment variables to disable buffering and configure Flask for production
ENV PYTHONUNBUFFERED=1 \
    FLASK_ENV=production \
    FLASK_APP=app.py \
    PATH="/opt/venv/bin:$PATH"

# Run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]
