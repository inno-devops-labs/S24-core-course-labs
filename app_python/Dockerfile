FROM python:3.9.18-alpine3.19

ARG USER_NAME=myuser

WORKDIR /myapp
COPY requirements.txt main.py /myapp/
RUN adduser -D $USER_NAME && chown -R $USER_NAME /myapp

USER $USER_NAME
EXPOSE 8080
RUN pip install --no-cache-dir --user -r requirements.txt

CMD ["python", "main.py"]
