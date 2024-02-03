# Stage 1: Build the application
FROM node:14-alpine as build
LABEL authors="evsey"
RUN adduser -D flaskuser
USER flaskuser
WORKDIR /app
COPY package*.json rollup.config.mjs ./
RUN npm install
COPY . .
RUN npm run build

# Stage 2: Create a lightweight runtime image
FROM node:14-alpine
LABEL authors="evsey"
RUN adduser -D flaskuser
USER flaskuser
WORKDIR /app
COPY --from=build /app/dist /app/dist
COPY package*.json ./
COPY views/index.ejs ./views/index.ejs
RUN npm install --only=production
EXPOSE 3000
CMD ["npm", "start"]
