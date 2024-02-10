FROM python:3-alpine3.15

# The environment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

LABEL version="1.0" description="WebApp showing current Moscow time" maintainer="rmolochko"

# Set the working directory to /app_python
WORKDIR /app_python

# Create user
RUN adduser -D user && chown -R user /app_python
USER user

# Copy files
COPY templates ./templates
COPY app.py requirements.txt ./

# Install dependencies
RUN pip install -r requirements.txt --no-cache-dir --user

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run app.py when the container launches
CMD ["python", "-m", "flask", "run", "--host", "0.0.0.0", "--port", "8080"]
