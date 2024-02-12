FROM python:3.11.1-slim

RUN ls

RUN adduser user

RUN mkdir -p /app && chown -R user:user /app

USER user

WORKDIR /app

COPY ./requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY ./templates/ ./templates 
COPY ./api/ .

EXPOSE 5001
CMD python ./main.py