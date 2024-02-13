# Use an official Python runtime as a parent image
FROM python:3.9-slim

WORKDIR /app_python

# Copy necessary files
COPY requirements.txt app.py /app_python/
COPY templates/ /app_python/templates/

RUN adduser --disabled-password appuser && chmod -R a-w+x+r /app_python

RUN pip3 install --no-cache-dir -r requirements.txt

USER appuser

EXPOSE 5000

# Run app.py when the container launches
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]