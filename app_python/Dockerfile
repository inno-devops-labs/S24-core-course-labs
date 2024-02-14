# syntax=docker/dockerfile:1

# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app_python

# Copy requirements.txt file into the container 
COPY requirements.txt  requirements.txt

# Create new user named user
RUN useradd user -m 

# Install requirements
RUN pip install --no-cache-dir -r requirements.txt

# Create directory for the user
RUN chown -R user:user /app_python

# switch to the user
USER user



# Copy app files and tests
COPY __init__.py __init__.py
COPY flaskr flaskr
COPY tests tests

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run the app
CMD ["flask", "--app", "flaskr/app", "run","--host=0.0.0.0"]
