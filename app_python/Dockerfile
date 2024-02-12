FROM python:3.9-alpine3.15

RUN adduser -D user
USER user

WORKDIR /app_python

COPY app.py requirements.txt ./

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]