FROM python:3.11.1-slim-bullseye

# Create a non-root user
RUN groupadd -r appuser && useradd -r -g appuser appuser

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install requirements separately (so no need for separate build stage)
COPY requirements.txt ./
RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN rm requirements.txt

# Copy the code separately, not touching the requirements
COPY ./app.py ./

# Change ownership of the application directory to the non-root user
RUN chown -R appuser:appuser /app

# Switch to the non-root user
USER appuser

# Indicate that the application needs port 8080 exposed
EXPOSE 8080

ENTRYPOINT ["python", "app.py"]
