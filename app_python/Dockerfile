FROM python:3.12-alpine3.18

ENV PYTHONUNBUFFERED 1

WORKDIR /app

# user
RUN addgroup -S group && adduser -S user -G group

# deps
COPY requirements.txt .
RUN pip install -r requirements.txt

ENV VISITS_FILE="visits.txt"
ENV VISITS_PATH="/app/visits"


RUN mkdir $VISITS_PATH && echo "0" > $VISITS_PATH/$VISITS_FILE
RUN chgrp -R group /app && chmod g+rw -R /app

USER user

# app
COPY app ./app


EXPOSE 8080

ENTRYPOINT ["python", "app/server.py"]