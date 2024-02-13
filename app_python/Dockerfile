FROM python:3.11-slim

WORKDIR /app

RUN useradd -m myuser && chown -R myuser /app
USER myuser

ENV PATH="/home/myuser/.local/bin:$PATH"

COPY requirements.txt main.py ./
COPY templates ./templates

RUN pip install --no-cache-dir --user -r /app/requirements.txt

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]