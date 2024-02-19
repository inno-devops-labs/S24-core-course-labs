# Docker Best Practices

In the Dockerfile for this application I have implemented several best practices to ensure security and efficiency:

1. Avoid unnecessary privileges:
   - The container runs as a non-root user to reduce the risk of privilege escalation.

2. Reduce attack surface:
   - Only necessary files and dependencies are included in the image (like "requirements.txt", "template" folder, "app.py")

3. Prevent confidential data leaks:
   - Sensitive information, such as credentials, is not hardcoded in the Dockerfile (.dockerignore used, "ADD" is not used in Dockerfile)

4. Others:
   - I followed best practices for optimizing the Docker image build process, such as using the slim-buster base image and caching dependencies.

For more details on Docker best practices, refer to the [Dockerfile Best Practices article](https://sysdig.com/blog/dockerfile-best-practices/).
