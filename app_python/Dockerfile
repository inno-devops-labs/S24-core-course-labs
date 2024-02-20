FROM python:3.11-slim

WORKDIR /app_python

RUN adduser --disabled-password user && chown -R user /app_python

USER user

COPY . /app_python
RUN pip install -r requirements.txt --no-cache-dir --user

EXPOSE 5000

CMD ["python", "main.py"]




