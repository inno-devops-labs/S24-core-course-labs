# Docker Best Practices

## Trusted Base Images
In our Dockerfile, we started with a trusted base image to ensure the security and reliability of our application. We used the official Python image as the base for our application.

## Latest and Secure Python Version
We made sure to use one of the latest and secure versions of Python in our Dockerfile to ensure the safety and stability of the application. This helps in keeping the application up-to-date with the latest security and bug fixes.

## Rootless container
To adhere to best security practices, we specified a non-root user to run commands within the Dockerfile. This minimizes the potential impact of security vulnerabilities by limiting the privileges of the running application.

## Minimal Images
We aimed to keep our Docker image minimal by only including the necessary dependencies and reducing the overall size of the image. This helps in optimizing resources and reducing the attack surface for potential security threats.

## COPY, not ADD
We followed the best practice of using the COPY command instead of ADD in our Dockerfile. COPY is more transparent and predictable in its behavior, making it a safer option for copying files into the Docker image.

## Hadolint Docker Linter
We implemented Hadolint as part of our Docker image creation process to ensure that our Dockerfile adheres to best practices and industry standards. This linter helps in identifying potential issues and enforcing best practices for Dockerfile creation.

Overall, we have employed these best practices to ensure the security, reliability, and efficiency of our Docker image and the application running within it. By following these practices, we aim to create a robust and secure environment for our application to operate in.

To build the image, run the following command:
```docker build -t my_app .```


To run the container, use the following command:
```docker run -p 5000:5000 my_app```