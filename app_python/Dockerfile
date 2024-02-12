# Use a base image that includes a non-root user
FROM python:3.9.18-alpine3.19

# Create a group and user
RUN addgroup -S app_python && adduser -S app_python -G app_python

# Change to the new user
USER app_python

# Set the working directory
WORKDIR /home/app_python

# Copy only the necessary files
COPY --chown=app:app requirements.txt ./
RUN pip install --no-cache-dir --upgrade -r requirements.txt --user

# Copy the application file
COPY --chown=app:app time_zone.py ./

# Expose the port the app runs on
EXPOSE  5000

# Run the application as the non-root user
ENTRYPOINT ["python", "time_zone.py"]
