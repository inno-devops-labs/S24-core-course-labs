FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN apt update -y && apt install -y curl
RUN pip3 install -r requirements.txt
RUN adduser app_user
RUN mkdir /logs && chown -R app_user:app_user /logs
ENV LOGS_FILE_PATH="/logs/moscow-time.log"
# RUN rm /bin/sh /bin/dash /bin/bash

COPY app/* /app/

USER app_user:app_user

EXPOSE 5000

ENTRYPOINT [ "flask", "--app", "main", "run", "--host=0.0.0.0" ]
