FROM python:3.11.5-alpine3.18

ENV PYTHONDONTWRITEBYTECODE=1

COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

RUN adduser app --system -S /bin/nologin -D -H
RUN mkdir /data && chown app /data
VOLUME [ "/data" ]
USER app
WORKDIR /app

COPY main.py .

ENV PORT="8000"
EXPOSE $PORT

CMD ["python", "main.py"]