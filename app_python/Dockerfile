FROM python:3.9.18-alpine3.18

LABEL description="A fastapi application to display the current time in Moscow" maintainer="ejedavid"

WORKDIR /app

# Limited noroot user permission
RUN adduser -D myuser && mkdir /app/app_python && chown -R myuser ./app_python

USER myuser

# User path is added to run user installed packages
ENV PATH="/home/myuser/.local/bin:$PATH"

# Enabling caching by copying the requirements first
COPY requirements.txt ./app_python/requirements.txt
RUN pip install -r ./app_python/requirements.txt --no-cache-dir --user

# Copy python files
COPY __init__.py app.py ./app_python/

# Bind uvicorn to port 8000 
CMD ["uvicorn", "app_python.app:app", "--host", "0.0.0.0", "--port", "8000"]