## Best practices that was employed
1. **Using .dockerignore File**: Large context can result in larger build time. You should use `.dockerignore` file in your project root to ignore files and directories that are not needed in the final image.
2. **Health Check**: Docker provides a HEALTHCHECK instruction to tell Docker how to test a container to check that it is still working.
3. **Non-privileged User**: Running your Docker container as a non-root user is creates an additional layer of security. If an attacker gains control over a container, being a non-root user limits the potential damage by preventing them from gaining complete control over the system. This approach aligns with the principle of least privilege, further enhancing your application's security.
4. **Address Graceful Shutdown**: Use `STOPSIGNAL` to change the system call signal that will be sent to the container to exit. This allows your app to gracefully stop and ensures that no data is lost or corrupted.
5. **Clean Up**: Clean up unnecessary system packages to keep the image size minimal.
6. **Minimize the Number of Layers**: Each `RUN`, `COPY`, and `ADD` command creates a new layer in the Docker image. So, I chained the command using `&&` operator.

