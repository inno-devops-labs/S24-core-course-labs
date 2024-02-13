# Using the Python Alpine image as the base image
FROM python:3.9.18-alpine3.19@sha256:7e53de21917d6793787bc67483838360404bb2fd70d9c3e38ccc243790c323b2

# Set the working directory in the container
WORKDIR /app

# Add a new non-root user
RUN adduser -D myuser && mkdir /app/app_python && chown -R myuser ./app_python
USER myuser

# Copy requirements.txt 
COPY requirements.txt ./app_python/requirements.txt

# Install dependencies
RUN pip install -r ./app_python/requirements.txt --no-cache-dir --user

# Copy only relevant files
COPY app/__init__.py ./app/__init__.py 
COPY app/routes.py ./app/routes.py 
COPY app/templates/index.html ./app/templates/index.html 
COPY static/style.css ./static/style.css 
COPY tests/__init__.py ./tests/__init__.py
COPY tests/test_flask_app.py ./tests/test_flask_app.py  

# Expose port 5000
EXPOSE 5000

LABEL maintainer="c.ogbonna@innopolis.university"
LABEL description="Docker image for Flask app."

# Run the app
CMD ["python3", "app/routes.py"]