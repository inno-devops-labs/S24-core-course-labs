FROM python:3.9.18-alpine3.18

LABEL version='1.0'

WORKDIR /app

RUN adduser -D puppet && chown -R puppet /app

COPY app.py config.py requirements.txt ./
COPY tests ./tests
COPY project ./project

USER puppet
RUN pip install --no-cache-dir --user -r requirements.txt

EXPOSE 5000

CMD ["python", "-m", "flask", "--app", "app", "run", "--host=0.0.0.0"]