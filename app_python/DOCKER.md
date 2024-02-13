## Docker security best practises
* the container is rootless: 
  * default root user is overloaded 
  * the executable file still belongs to the root user 
  * I did not bind to a specific UID 
* the base image is trustworthy. The image is an official openjdk image 
* the version is fixed 
* `bash` and `sh` are removed from the container, so nobody can exec into it