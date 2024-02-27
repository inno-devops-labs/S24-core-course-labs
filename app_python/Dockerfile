FROM python:3.9-alpine3.15

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

RUN adduser -D myuser

USER myuser

CMD ["python", "time_web.py"]
