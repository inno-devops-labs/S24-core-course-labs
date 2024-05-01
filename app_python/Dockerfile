FROM python:3.11-slim-buster

WORKDIR /app
RUN mkdir -p /app/data

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY index.html .
COPY app.py .

RUN useradd vlad
RUN chown -R vlad:vlad /app/data
RUN chown -R vlad .
USER vlad

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

