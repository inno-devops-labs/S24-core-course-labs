FROM python:3.12-alpine3.18

ENV PYTHONUNBUFFERED 1

WORKDIR /app

# user
RUN addgroup -S group && adduser -S user -G group

# deps
COPY requirements.txt .
RUN pip install -r requirements.txt

RUN echo "0" > /app/visits.txt
RUN chgrp -R group /app
RUN chmod g+rw -R /app

USER user

# app
COPY app ./app


EXPOSE 8080

ENTRYPOINT ["python", "app/server.py"]