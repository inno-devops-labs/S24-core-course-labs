FROM python:3.9.18-alpine3.19

WORKDIR /app_python

COPY app.py requirements.txt /app_python/

RUN adduser -D myuser && chown -R myuser /app_python

USER myuser

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]