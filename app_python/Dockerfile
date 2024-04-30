# Stage 1: Build stage for multistage build (if applicable)
# This stage is optional and depends on whether your application requires compilation or a build process
FROM python:3.9.18-alpine3.19@sha256:7e53de21917d6793787bc67483838360404bb2fd70d9c3e38ccc243790c323b2

WORKDIR /work_app

RUN adduser -D appuser
RUN mkdir /work_app/app /work_app/visits_folder && chown -R appuser:appuser /work_app/app /work_app/visits_folder

USER appuser

# Install build dependencies (if any)
# For a Python app, you might not have a compilation step, but you may need to install dependencies here
COPY requirements.txt ./app_python/requirements.txt

RUN pip install -r ./app_python/requirements.txt --no-cache-dir --user

ADD app ./app
COPY ./config.py .
COPY ./run.py .
COPY ./test_app.py .

# Expose port and define entrypoint
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=run.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run app.py when the container launches
CMD python -m flask run
