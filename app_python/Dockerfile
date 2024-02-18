WORKDIR /app

# Copy requirements.txt into the container at /app
COPY app_python/requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Change working directory to /app/app_python
WORKDIR /app/app_python

# Copy the rest of the application code into the container at /app/app_python
COPY . .

# Switch back to /app
WORKDIR /app

# Create a non-root user
RUN adduser -D myuser

# Switch to the non-root user
USER myuser

# Expose port 5000 to the outside world
EXPOSE 5000

# Command to run the application
CMD ["python", "-u", "app.py"]