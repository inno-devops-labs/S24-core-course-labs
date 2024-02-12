# Use Python 3.9.18 slim-bullseye image
FROM python:3.9.18-slim-bullseye

# Set working directory to /app_python
WORKDIR /app_python

# Create non-root user 'app' and set directory ownership
RUN adduser app && chown -R app /app_python
USER app

# Copy current directory contents to /app_python
COPY . /app_python

# Install Python dependencies from requirements.txt
RUN pip install --user -r requirements.txt --no-cache-dir

# Expose port 5000
EXPOSE 5000

# Set default command
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
