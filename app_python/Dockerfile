FROM python:3.10.13-alpine3.19

WORKDIR /app

RUN adduser -D python && chown -R python /app

COPY requirements.txt ./
COPY src ./src

USER python:python
RUN pip install -r requirements.txt --no-cache-dir --user

EXPOSE 8080

CMD ["python", "src/app.py"]