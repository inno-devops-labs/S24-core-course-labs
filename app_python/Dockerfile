# Use a minimal base image
FROM python:3.9-slim as builder

# Install dependencies
RUN pip install --upgrade pip && \
    pip install --no-cache-dir pipenv

# Copy Pipfile and Pipfile.lock
COPY Pipfile Pipfile.lock ./

# Install project dependencies
RUN pipenv install --system --deploy

# Start a new, final image to reduce size
FROM python:3.9-slim as final

# Create a non-root user
RUN useradd -m myuser

# Switch to the non-root user
USER myuser

# Copy the dependencies from the builder image
COPY --from=builder /usr/local/lib/python3.9/site-packages/ /usr/local/lib/python3.9/site-packages/

# Copy the application code to the container
COPY . .

# Run the application
CMD ["python", "app.py"]