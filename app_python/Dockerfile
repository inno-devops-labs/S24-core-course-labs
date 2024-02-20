FROM python:3.11-slim

WORKDIR /app_python

RUN adduser --disabled-password user && chown -R user /app_python

USER user

COPY ./requirements.txt /app_python/
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . /app_python
EXPOSE 5000

CMD ["python", "main.py"]