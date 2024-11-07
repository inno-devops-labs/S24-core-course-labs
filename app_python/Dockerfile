FROM python:3.9-alpine

WORKDIR /app

RUN adduser -D test && chown -R test /app
USER test

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]