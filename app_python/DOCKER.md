# Best practices employed within Dockerfile
1. Use Specific Base Image:

    Employed a specific version of the base image (python:3.9-alpine) to ensure consistency and stability across builds.
2. Minimize Layers:

    Combined multiple commands into single RUN and COPY instructions to reduce the number of layers, optimizing image size and build time.
3. Efficient Copying of Files:

    Used COPY command with appropriate source and destination paths to efficiently copy only necessary files (app.py and templates/ directory) into the image, minimizing unnecessary files.
4. Dependency Management:

   Utilized a requirements.txt file to manage dependencies and installed them in a single RUN instruction with pip install --no-cache-dir to prevent caching of downloaded packages and reduce image size.
5. Security Considerations:

   Ran the container as a non-root user by creating a dedicated user (userwithoutroot) within the container, enhancing security by reducing the attack surface.
Applied user ownership (--chown=userwithoutroot:userwithoutroot) to copied files to ensure they are owned by the non-root user.

6. Expose Specific Ports:

   Exposed only the necessary port (5000) using the EXPOSE instruction, providing clarity on the intended network interface.
