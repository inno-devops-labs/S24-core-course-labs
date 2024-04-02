FROM python:3-alpine3.15

WORKDIR /app_python

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

RUN adduser -D myuser

USER myuser

CMD ["python", "app.py"]