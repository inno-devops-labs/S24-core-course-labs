FROM python:3.11

# The environment variable ensures that the python output is set straight
# to the terminal without buffering it first
ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

LABEL version="1.0" description="WebApp showing current Moscow time" maintainer="rmolochko"

# Set the working directory to /app_python
WORKDIR /app

# Create user
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser && chown -R appuser /app

# Copy requirements.txt
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

USER appuser

# Copy files
COPY templates ./templates
COPY app.py app.py

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run app.py when the container launches
CMD ["python", "-m", "flask", "run", "--host", "0.0.0.0", "--port", "8080"]
