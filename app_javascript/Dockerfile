FROM node:14.21.3-alpine3.17 as builder

WORKDIR /app

COPY package*.json app.js ./
COPY views ./views

RUN npm install \
    && npm install -g pkg@5.4.0 \
    && pkg app.js --target node14-alpine-x64

FROM alpine:3.17

WORKDIR /app

COPY --from=builder /app/app ./app
COPY --from=builder /app/views ./views

EXPOSE 3000

RUN adduser -D myuser
USER myuser

CMD ["./app"]
