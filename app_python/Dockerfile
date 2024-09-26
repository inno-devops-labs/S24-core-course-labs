FROM python:3.9-slim

WORKDIR /app

COPY src/main.py /app/src/main.py
COPY requirements.txt /app/

RUN pip install -r requirements.txt

EXPOSE 8000

CMD [ "python", "src/main.py", "0.0.0.0", "8000" ]