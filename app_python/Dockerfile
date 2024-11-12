FROM python:3.11.7-alpine

RUN adduser -D app
RUN apk add curl --no-cache

WORKDIR /src
EXPOSE 8080/tcp

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY __main__.py ./server/

USER app
CMD ["python3", "-m", "server"]
HEALTHCHECK --interval=1s \
  CMD curl -f http://localhost:8080/ || exit 1
