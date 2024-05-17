FROM python:3.11.8-alpine3.18

RUN adduser -D appuser
RUN mkdir -p /app
RUN chown -R appuser /app

USER appuser

WORKDIR /app

COPY requirements.txt ./
COPY ./ptime ./ptime/

RUN pip install -r requirements.txt

EXPOSE 8080

CMD python ./ptime/main.py