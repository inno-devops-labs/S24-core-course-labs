# Continuous Integration (CI)

## Best practices used:

- ### Confidential Data
  I used secrets to handle sensitive information, such as Docker Hub tokens. This helped to keep my confidential
  data secure.
- ### Job Timeout
  It is always good idea to set a custom timeout for your jobs to prevent them from running indefinitely in case of
  errors or issues.
- ### Caching
  I utilized caching to speed up my builds by storing and reusing frequently used data.
- ### Dependency Management
  It is always a good idea to use specific versions for your dependencies to ensure the consistency and reproducibility
  of your builds.
- ### Trusted Actions
  I used only trusted actions in my CI pipeline to avoid potential security risks.
- ### DockerHub Push
  I only pushed to DockerHub when all my tests were passing. This ensured that my images are stable and
  tested.