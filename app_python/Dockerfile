FROM python:3.9.18-slim-bullseye

WORKDIR /app

RUN useradd app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt && rm requirements.txt

COPY main.py /app/

RUN chmod 444 /app/main.py

RUN mkdir /app/vol
RUN chown -R app:app /app

USER app

EXPOSE 8080

ENTRYPOINT ["python3", "main.py"]
