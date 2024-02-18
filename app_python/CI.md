## Best Practices of CI Workflow

The following best practices were used for efficient CI workflow:

- Setup environment variables: Environment variables are used to store sensitive information, 
such as API keys or credentials, that are needed during the CI process.
GitHub Secrets are configured to securely store and access these variables in the workflow.
- Caching: cache is used to speed up the workflow by storing dependencies and build artifacts between workflow runs. 
- Linting: `flake8` linting helps ensure that code follows a consistent style and adheres to best practices.
- Testing: Unit tests are used to ensure that code functions as expected.
- Docker deployment: Docker image is automatically built and pushed to dockerhub on successful pass of all other CI jobs.