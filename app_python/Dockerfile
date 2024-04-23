# Use an official Python runtime as a base image
FROM python:3.9.18-alpine3.18

LABEL description="Python app that shows the time in Moscow timezone"

# Create a non-root user and group
RUN adduser -D myuser
USER myuser

# Set the working directory inside the container
WORKDIR /app_python

# Copying the files
COPY --chown=myuser:myuser app.py requirements.txt visits.txt /app_python/
COPY --chown=myuser:myuser templates /app_python/templates

RUN pip install -r /app_python/requirements.txt --no-cache-dir --user


# Expose the port the app runs on
EXPOSE 8000

CMD ["python", "/app_python/app.py", "--host", "0.0.0.0"]