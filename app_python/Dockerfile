FROM python:3.11.5-alpine3.18

ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir

COPY main.py .

RUN adduser app --system -D
USER app

ENV PORT="8000"
EXPOSE $PORT

CMD ["python", "main.py"]