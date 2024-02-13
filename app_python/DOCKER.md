## Docker

### Best Practices

- **_Non-Root User_**  
  I created a non-root user to run the application within the container, enhancing security by reducing the privileges
  of the running process.

- **_Layer Sanity_**  
  I build the Dockerfile in such a way as to utilize Docker's layer caching mechanism, ensuring that only the
  appropriate layers are rebuilt when changes are made.

- **_COPY Specific Files_**  
  I use the COPY instruction to copy only necessary files into the Docker image, reducing the risk of including
  unnecessary or sensitive information.

- **_Specific Version of Base Image_**  
  I specify a precise version of the Python base image to ensure consistency and avoid potential vulnerabilities
  introduced by using the latest version.

- **_.dockerignore_**  
  I use the .dockerignore file to prevent unnecessary files and directories from being copied into the Docker image,
  reducing its size and potential security risks.

- **_Exposed Ports_**  
  I explicitly set only the port that the application needs to communicate.
