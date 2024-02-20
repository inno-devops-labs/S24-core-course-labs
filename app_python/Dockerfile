FROM python:3.11-slim

WORKDIR /app_python

RUN adduser --disabled-password user && chown -R user /app_python

USER user

COPY . /app_python
RUN pip install --no-cache-dir --upgrade -r /app_python/requirements.txt

EXPOSE 5000

CMD ["python", "main.py"]




