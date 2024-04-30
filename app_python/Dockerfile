FROM python:3-alpine3.15

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY time_web.py .

EXPOSE 5000

CMD ["python", "time_web.py"]
