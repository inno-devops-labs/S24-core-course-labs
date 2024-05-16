# Stage  1: Build the TypeScript code
FROM node:14-alpine AS builder
WORKDIR /app

# Copy only the necessary files for building the application
COPY package*.json ./
COPY tsconfig.json ./
COPY src/ ./src/

# Install dependencies and build the application
RUN npm ci
RUN npm run build

# Stage  2: Set up the runtime environment
FROM node:14-alpine
WORKDIR /app

# Copy only the necessary files for running the application
COPY --from=builder /app/dist ./dist
COPY package*.json ./
COPY public/ ./public/

# Install production dependencies
RUN npm ci --only=production

# Create a non-root user for security
RUN adduser -D myuser
USER myuser

# Expose the port the app runs on
EXPOSE  3000

# Start the application
CMD ["npm", "run", "start:prod"]
