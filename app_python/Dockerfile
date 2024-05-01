FROM python:3.11.8-alpine3.19

WORKDIR /app

# Create a group and user
RUN addgroup -S appgroup && adduser -S appuser -G appgroup && \
    chown -R appuser /app
USER appuser

# To use uvicorn executable in future
ENV PATH /home/appuser/.local/bin:${PATH}

# Copy separately for better caching on rebuilding
COPY ./requirements.txt /app/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copy main app
COPY . .

# Run it
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]