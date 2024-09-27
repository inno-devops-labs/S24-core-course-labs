FROM node:18-alpine3.19@sha256:aacbcec05180c1dd8c33dba8a9c42b75dbfdd659aa57617497f1ce2c5d83d889

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

RUN npm run build

CMD ["npm", "run", "preview"]
