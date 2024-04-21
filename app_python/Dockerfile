FROM python:3-alpine3.15

# The environment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE=1

LABEL version="1.0" description="WebApp showing current Moscow time" maintainer="rmolochko"

# Set the working directory to /app_python
WORKDIR /app_python

# Create user
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser && chown -R appuser /app_python


RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

USER appuser

# Copy files
COPY templates ./templates
COPY app.py requirements.txt ./

RUN mkdir /app/data && touch /app/data/visits.txt && chown -R appuser:appuser /app

# Make port 8080 available to the world outside this container
EXPOSE 8080

# Run app.py when the container launches
CMD ["python", "-m", "flask", "run", "--host", "0.0.0.0", "--port", "8080"]
