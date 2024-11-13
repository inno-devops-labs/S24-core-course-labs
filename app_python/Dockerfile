FROM python:3.9.6-alpine

# Create a user for running the application (non-root user)
RUN adduser -D myuser

# Set the working directory inside the container
WORKDIR /app_python

# Copy only the necessary files into the container
COPY requirements.txt /app_python/
COPY app.py /app_python/

# Change ownership of the application directory to the new user
RUN chown -R myuser /app_python

# Switch to the non-root user
USER myuser

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port on which the app will run
EXPOSE 5000

# Define the command to run your application
CMD ["python3", "app.py"]

