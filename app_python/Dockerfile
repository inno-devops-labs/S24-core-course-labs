FROM python:3.11.6-alpine3.18

ARG USER_NAME=myuser

EXPOSE 5000
WORKDIR /app
COPY requirements.txt main.py /app/
# Create user and set ownership and permissions as required
RUN adduser -D $USER_NAME && chown -R $USER_NAME /app
# ... copy application files
USER $USER_NAME
RUN pip install --no-cache-dir --user -r requirements.txt

CMD ["python", "main.py"]