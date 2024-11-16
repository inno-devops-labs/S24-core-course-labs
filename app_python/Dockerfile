FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt .
COPY . .

EXPOSE 5000

RUN adduser -D test && chmod 777 /app

RUN pip install --no-cache-dir -r requirements.txt && chmod 777 visits.txt

USER test

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]