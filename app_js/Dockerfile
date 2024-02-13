
FROM node:14-alpine

WORKDIR /app_js


COPY package.json package-lock.json app.js ./
COPY views/ ./views/
RUN adduser --disabled-password appuser && \
    npm install && \
    chown -R appuser:appuser /app_js

USER appuser

EXPOSE 3000

CMD [ "node", "app.js" ]
