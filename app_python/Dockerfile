FROM python:3.9-alpine3.18

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN addgroup -S nonroot && adduser -S nonroot -G nonroot

WORKDIR /app

RUN chown nonroot:nonroot /app

USER nonroot

COPY requirements.txt .
COPY app.py .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]
