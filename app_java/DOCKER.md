## Docker security best practises
* the container is rootless:
  * default root user is overloaded
  * the executable file still belongs to the root user
  * I did not bind to a specific UID
* the base image is trustworthy. This image is granted a title of "The Docker official image" that (according to the
  Docker) a curated Docker open source and drop-in solution repository that follows the best practices
* the version is fixed
* `bash` and `sh` are removed from the container, so nobody can exec into it
* layer sanity is preserved and only the executable jar file is transferred to the run layer from the build layer