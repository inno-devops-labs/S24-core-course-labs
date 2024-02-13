# Docker

---

## Used Best Practices

1. Execute app as non-root user
2. Specific version of base image
3. All not likely to change commands are above copy of files of projects (if possible)
4. Only specific files are copied
5. App files are not writable (only read + execute or just read)
6. Docker ignore file for target and specific markdown files (Files that are not needed to execute app)
7. Multistage build is used (docker image decreased by almost 90%)
