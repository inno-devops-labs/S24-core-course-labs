# Docker Best Practices

[![Node.js CI](https://github.com/zeyadAjamy/S24-core-course-labs/actions/workflows/javascript-ci.yaml/badge.svg?branch=lab3)](https://github.com/zeyadAjamy/S24-core-course-labs/actions/workflows/javascript-ci.yaml)

1. **Use a specific Node.js version as the base image**: Utilizing a specific Node.js version (`node:18-bullseye`) ensures consistency and avoids unexpected behavior due to version differences. It also allows for better reproducibility of builds.

2. **Create a non-root user**: Creating a non-root user (`appuser`) enhances security by minimizing potential security risks associated with running the application as the root user. This follows the principle of least privilege, limiting access to only the necessary resources.

3. **Switch to the non-root user**: Switching to the `appuser` after creating it further reduces the attack surface of the container by restricting the execution of the application to a non-privileged user context.

4. **Set the working directory and assign ownership to the non-root user**: Setting the working directory (`/app`) and assigning ownership to the `appuser` ensures that subsequent commands operate within the correct context and with the appropriate permissions, improving security and stability.

5. **Copy only the package.json file to avoid unnecessary files in the build context**: Copying only the `package.json` file into the Docker image reduces the size of the build context, which improves build performance and minimizes the risk of including sensitive or unnecessary files.

6. **Install the required packages as the non-root user**: Installing required packages (`package.json` dependencies) as the `appuser` prevents potential security risks associated with running npm commands as the root user. Using `--mount=type=cache` for npm caching optimizes the build process by caching dependencies, enhancing build speed and efficiency.

7. **Copy the application files**: Copying the application files (`app.js`) into the Docker image ensures that the necessary code is available for execution within the container.

8. **Set a build argument for the port**: Setting a build argument (`PORT`) for the port number allows flexibility in specifying the port at build time, enhancing customization without modifying the Dockerfile directly.

9. **Expose the port**: Exposing the port (`$PORT`) in the Dockerfile documents the port that the containerized application listens on, making it easier for users to understand and interact with the container.

10. **Specify the command to run the Node.js application**: Specifying the command (`CMD`) to run the Node.js application (`node app.js`) ensures that the container starts the application as the default behavior, simplifying container execution and facilitating ease of use for users.
