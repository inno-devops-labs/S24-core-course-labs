FROM python:3.10.1-alpine3.15
LABEL authors="Ilnur"

# Exposing port for app
EXPOSE 5000

# Creating user to switch from root after
RUN adduser -D myuser

# Copy requirements to directory
COPY requirements.txt /app_data/requirements.txt
RUN pip install -r /app_data/requirements.txt

# Copy files to directory
COPY main.py /app_data/main.py
COPY fast_api_app.py /app_data/fast_api_app.py

RUN mkdir -p /app_data/api/v1/time
RUN mkdir -p /app_data/api/v1/visits
RUN mkdir -p /app_data/visits

COPY api/__init__.py /app_data/api/__init__.py
COPY api/v1/__init__.py /app_data/api/v1/__init__.py
COPY api/v1/time/__init__.py /app_data/api/v1/time/__init__.py
COPY api/v1/time/schemas.py /app_data/api/v1/time/schemas.py
COPY api/v1/time/views.py /app_data/api/v1/time/views.py
COPY api/v1/visits/__init__.py /app_data/api/v1/visits/__init__.py
COPY api/v1/visits/schemas.py /app_data/api/v1/visits/schemas.py
COPY api/v1/visits/crud.py /app_data/api/v1/visits/crud.py

# Change to read-only (With new permissions should be write + read)
RUN chmod -R 555 /app_data && chmod -R 777 /app_data/visits

# Changing user
USER myuser

WORKDIR /app_data

ENTRYPOINT ["python3", "main.py"]