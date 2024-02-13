FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN adduser app_user
RUN rm /bin/sh /bin/dash /bin/bash

COPY app/* /app/

USER app_user:app_user

ENTRYPOINT [ "flask",  "--app", "main", "run" ]
