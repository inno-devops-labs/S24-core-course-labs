FROM python:3.11.1-slim

WORKDIR /app

RUN adduser user && mkdir -p /app && chown -R user:user /app

USER user

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt && rm requirements.txt

COPY ./templates/ ./templates 
COPY ./api/ .

EXPOSE 5001
CMD python ./main.py