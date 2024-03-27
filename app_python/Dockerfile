# Use an exact version of the Python image for consistency
FROM python:3.12.1

# Set environment variables for Python to run in unbuffered mode and not write .pyc files
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Create a directory to hold the application code inside the image
WORKDIR /app

# Copy only the requirements file and install Python dependencies
# Also create a non-root user in same command to reduce the number of layers
COPY requirements.txt /app
RUN useradd -m myuser && chown -R myuser /app

# Install Python requirements
RUN pip install --upgrade pip && \
    pip install --upgrade -r ./requirements.txt

# Copy the rest of the application code
COPY . /app

# Switch to non-root
USER myuser

# Expose the port the app runs on
EXPOSE 5000

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
