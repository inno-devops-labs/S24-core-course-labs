# Stage 1: Build stage for multistage build (if applicable)
# This stage is optional and depends on whether your application requires compilation or a build process
FROM python:3.8-slim as builder
WORKDIR /work_app
# Install build dependencies (if any)
# For a Python app, you might not have a compilation step, but you may need to install dependencies here
COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /work_app/wheels -r requirements.txt

# Stage 2: Final stage to create a slimmed-down image
FROM python:3.8-slim
# Create a non-root user
RUN useradd --create-home appuser
WORKDIR /work_app
# Copy only the necessary artifacts from the builder stage
COPY --from=builder /work_app/wheels /wheels
COPY --from=builder /work_app/requirements.txt .
# Install runtime dependencies using artifacts from the build stage
RUN pip install --no-cache /wheels/* \
    && rm -rf /wheels \
    && rm -rf /root/.cache/pip/*
# Copy the source code (or built application artifacts) last, to take advantage of layer caching
ADD app /work_app/app
COPY ./config.py .
COPY ./run.py .
COPY ./test_app.py .

# Switch to non-root user
USER appuser

# Expose port and define entrypoint
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=run.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run app.py when the container launches
CMD ["flask", "run"]
