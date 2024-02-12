FROM python:3.11-slim

WORKDIR /app

RUN useradd -d /app fastapi && chown -R fastapi:fastapi /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

USER fastapi

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
