FROM python:3.8-alpine3.15 as base

WORKDIR /app_python

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

FROM base as runtime

COPY . .

EXPOSE 5000

RUN adduser -D myuser

USER myuser

CMD ["python", "-u", "app.py"]