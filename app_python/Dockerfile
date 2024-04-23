# Use an official Python runtime as a parent image
FROM python:3.9-slim

WORKDIR /app_python

# Copy necessary files
COPY requirements.txt app.py /app_python/
COPY templates/ /app_python/templates/

RUN mkdir /app_python/data && chown -R ${USER}:${USER} /app_python


RUN pip3 install --no-cache-dir -r requirements.txt

USER ${USER}

EXPOSE 5000

# Run app.py when the container launches
CMD ["python3", "app.py"]