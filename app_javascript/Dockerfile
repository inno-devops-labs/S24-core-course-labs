FROM node:14.21.3-alpine3.17

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY app.js ./
COPY views ./views
COPY visits ./visits

EXPOSE 3000

RUN adduser -D myuser \
    && chown -R myuser:myuser /app

USER myuser

CMD ["node", "app.js"]
