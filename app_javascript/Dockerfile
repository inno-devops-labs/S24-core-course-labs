FROM node:18-bullseye AS base

# Create a non-root user
RUN adduser --system --group appuser

# Switch to the non-root user
USER appuser

# Set the working directory and assign ownership to the non-root user
WORKDIR /app
RUN chown -R appuser:appuser /app

# Copy only the package.json file to avoid unnecessary files in the build context
COPY --chown=appuser:appuser package.json .

# Install the required packages as the non-root user
RUN --mount=type=cache,target=/root/.npm \
    npm install --no-cache

# Copy the application files
COPY --chown=appuser:appuser app.js .

# Set a build argument for the port
ARG PORT=5000

# Expose the port
EXPOSE $PORT

# Specify the command to run the Node.js application
CMD ["node", "app.js"]
