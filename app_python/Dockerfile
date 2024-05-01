# Use a specific version of the python image with specific sha256 hash
FROM python:3.9.18-alpine3.19@sha256:7e53de21917d6793787bc67483838360404bb2fd70d9c3e38ccc243790c323b2

# Set environment variables
ENV APP_HOME /app_python

# Set working directory
WORKDIR $APP_HOME

# Copy only necessary files and directories
COPY requirements.txt app.py $APP_HOME/
COPY templates/ $APP_HOME/templates/
COPY data/ $APP_HOME/data/

# Create a non-root user and remove write permissions for the group and others
RUN adduser --disabled-password appuser && chmod -R a-w+x+r $APP_HOME

# Switch to the non-root user and install the dependencies
USER appuser
RUN pip3 install --no-cache-dir -r requirements.txt

# Expose port 5000
EXPOSE 5000

# Command to run the application
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]