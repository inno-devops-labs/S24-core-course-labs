# Use an official Node.js runtime as a base image
FROM node:14-alpine

LABEL description="JavaScript app that serves time in Moscow timezone"

# Create a non-root user and group
RUN adduser -D myuser
USER myuser

# Set the working directory inside the container
WORKDIR /app_js

# Copying the files
COPY --chown=myuser:myuser app.js /app_js/

# Install dependencies (Express.js)
RUN npm init -y && npm install express

# Expose the port the app runs on
EXPOSE 3000

# CMD to start the Express.js server
CMD ["node", "/app_js/app.js"]