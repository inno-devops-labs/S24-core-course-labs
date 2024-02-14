FROM python:3.11.5-alpine3.18

EXPOSE 8080

ARG GROUP_NAME=appgroup
ARG USER_NAME=appuser

RUN addgroup -S $GROUP_NAME && adduser -S $USER_NAME -G $GROUP_NAME

USER $USER_NAME
WORKDIR /app_python

COPY requirements.txt .
COPY app.py .

RUN pip install --user -r requirements.txt


ENTRYPOINT ["python", "app.py"]
