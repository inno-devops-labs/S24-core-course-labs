## Dockerfile Best Practices

### 1. Using Official Base Image
- The Dockerfile utilizes the official Node.js image as the base image (`node:alpine`). Leveraging official images ensures reliability and compatibility with the intended runtime environment.

### 2. Creating New Group and User
- A new group (`mygroup`) and user (`myuser`) are created using the `addgroup` and `adduser` commands, respectively. This practice enhances security by running the application with restricted privileges.

### 3. Setting Working Directory
- The `WORKDIR` instruction sets the working directory within the container to `/home/myuser`. Establishing a specific working directory simplifies subsequent commands and ensures consistency across different environments.

### 4. Copying Package Files
- The `COPY` instruction copies the `package.json` and `package-lock.json` files to the working directory, ensuring that only necessary files are included. Additionally, file ownership is explicitly set to `myuser:mygroup` to maintain proper permissions.

### 5. Dependency Installation
- Dependencies are installed using `npm install --quiet --no-cache`. The `--quiet` flag suppresses unnecessary output, while `--no-cache` avoids caching of downloaded packages, enhancing efficiency and reproducibility.

### 6. Copying Application Files
- Only relevant application files are copied into the container. This includes the main application file (`app.js`) and any other necessary assets.

### 7. Exposing Port
- The `EXPOSE` instruction exposes port 3000, which is typically used by Node.js applications to serve HTTP requests. This allows external access to the application running within the container.

### 8. Adding Metadata
- Metadata is added to the image using `LABEL`, including the maintainer's email address (`maintainer="c.ogbonna@innopolis.university"`) and a brief description of the image's purpose (`description="Docker image for js app."`).

### 9. Defining Default Command
- The `CMD` instruction specifies the default command to run when the container starts. In this case, it runs the Node.js application by executing `node app.js`.

### 10. .dockerignore
- The project uses a `.dockerignore` file to exclude certain files and directories from being copied into the Docker image.