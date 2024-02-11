FROM python:3.11-slim

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN adduser --disabled-password app && pip install --no-cache-dir -r requirements.txt
COPY start.sh /usr/src/app/

COPY ./app ./app
RUN chmod -R a-w+x+r /usr/src/app 

USER app
EXPOSE 8000
ENV PYTHONPATH .

ENTRYPOINT ["bash", "start.sh"]