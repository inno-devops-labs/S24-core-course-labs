# syntax=docker/dockerfile:1

# Step 1: Building
FROM python:3-alpine3.15 as builder

WORKDIR /app_python

# Copy requirements.txt and install modeles
COPY requirements.txt .
RUN pip install --upgrade pip \
    pip install --no-cache-dir -r requirements.txt

# Copy source code
COPY . .

CMD [ "python3", "-m" , "app"]