FROM python:3.10

WORKDIR /app
EXPOSE 5000
COPY requirements.txt *.py /app/
RUN ["pip", "install", "-r", "requirements.txt"]
CMD ["python", "main.py"]
