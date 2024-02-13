FROM python:3.9-slim

# Create a non-root user and set permissions
RUN useradd appuser && mkdir /app && chown -R appuser /app

# Set the working directory in the container
WORKDIR /app

# Copy necessary files
COPY --chown=appuser:appuser . /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 5000

# Run app.py when the container launches
CMD ["python", "task1.py"]
