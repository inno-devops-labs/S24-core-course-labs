FROM python:3.11.6-alpine3.18

EXPOSE 8080

ARG GROUP_NAME=appgroup
ARG USER_NAME=appuser

RUN addgroup -S $GROUP_NAME && adduser -S $USER_NAME -G $GROUP_NAME

USER $USER_NAME
WORKDIR /app

COPY templates ./templates
COPY static ./static
COPY requirements.txt .
COPY main.py .

RUN pip install --user -r requirements.txt


ENTRYPOINT ["python", "main.py"]

