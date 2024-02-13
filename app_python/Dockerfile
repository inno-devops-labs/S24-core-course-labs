FROM python:3.12.2-alpine3.19
WORKDIR /app

RUN adduser -D app && chown -R app /app

COPY requirements.txt .
RUN pip3.12 install -r requirements.txt
COPY src/ src/

USER app
CMD ["python3.12", "src/main.py"]
EXPOSE 8080
