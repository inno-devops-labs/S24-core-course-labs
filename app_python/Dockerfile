FROM python:3.9-slim

WORKDIR /app

RUN adduser --disabled-password app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

USER app

EXPOSE 5000

ENV FLASK_ENV=production

CMD ["python", "application.py", "runserver", "--host", "0.0.0.0"]

