# Using the official Node.js image as the base image
FROM node:alpine

# Add a new group and user
RUN addgroup mygroup && adduser -S -G mygroup myuser

# Switch to the new user
USER myuser

# Set the working directory in the container
WORKDIR /home/myuser

# Copy package.json and package-lock.json to the working directory
COPY --chown=myuser:mygroup package*.json ./

# Install dependencies
RUN npm install --quiet --no-cache

# Copy only relevant files
COPY app.js .
COPY views/index.ejs ./views/index.ejs
COPY test ./test/test.js 

# Expose port 5001
EXPOSE 5001

LABEL maintainer="c.ogbonna@innopolis.university"
LABEL description="Docker image for js app."

# Run the app
CMD ["node", "app.js"]