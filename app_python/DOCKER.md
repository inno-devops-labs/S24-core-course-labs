# Docker

---

## Used Best Practices

1. Execute app as non-root user
2. Specific version of base image
3. All not likely to change commands are above copy of
   files of projects (if possible)
4. Only specific files are copied
5. App files are not writable (only read + execute)
6. Docker ignore file for cache files and
   venv and tests folder (Files that are not needed to execute app)
