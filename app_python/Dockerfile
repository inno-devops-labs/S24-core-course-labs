FROM python:3.11-slim

COPY requirements.txt .

RUN pip install --user -r requirements.txt

COPY ./ /app

WORKDIR /app

EXPOSE 5000

CMD [ "python", "-u", "app.py"]