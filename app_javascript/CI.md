# CI and Best Practices

When writing GitHub Actions workflow for the application, I followed the best practices:

- I used `push` and `pull_request` triggers and specified paths and branches that should trigger the workflow, so that the workflow runs only when necessary.
- When testing application, I used a matrix strategy to run the tests on different versions of NodeJS.
- I configured Node using official GitHub Actions that also includes the `pnpm` caching capability.
- I splitted the workflow into multiple jobs to run the tests and security checks in parallel, while the build job runs only if the tests pass.
- I used secrets to store sensitive data, such as the Docker Hub and Snyk tokens.
