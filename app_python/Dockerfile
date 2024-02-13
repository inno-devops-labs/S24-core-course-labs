FROM python:3.11.8-alpine3.19

COPY main.py requirements.txt /app_python/

RUN adduser -D myuser && chown -R myuser /app_python
USER myuser
WORKDIR /app_python
RUN pip install -r requirements.txt
CMD ["/home/myuser/.local/bin/uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]
