# syntax=docker/dockerfile:1

# Official image
FROM python:3.10.0-alpine

# Working directory
WORKDIR /app_python

# User
RUN adduser -D sapushha && chown -R sapushha /app_python
USER sapushha

# Copy of necessary files
COPY templates ./templates
COPY app.py requirements.txt ./

# Dependencies
RUN pip install -r requirements.txt --no-cache-dir --user

# Run the application
EXPOSE 8080
CMD [ "python", "-m", "flask", "run", "--host", "0.0.0.0", "--port", "8080"]