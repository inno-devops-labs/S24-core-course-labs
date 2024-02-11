FROM node:15-alpine
WORKDIR /usr/src/app
RUN apk add --no-cache bash
RUN npm install
RUN npm install -g live-server  
COPY index.html ./
COPY app.js ./
EXPOSE  8080
RUN adduser -D user && chown -R user /usr/src/app  
USER user
CMD ["live-server", "--port=8080", "--host=0.0.0.0"]