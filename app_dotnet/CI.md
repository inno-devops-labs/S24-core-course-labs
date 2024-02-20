## CI best practices

1. **Descriptive Job Names**: Each job has a clear and descriptive name (build and docker), making it easier to understand the purpose of each job.

2. **Separation of Concerns with Jobs**: The workflow is divided into separate jobs (build and docker), allowing for better organization and parallel execution if needed.

3. **Environment Variables**: The IMAGE_NAME environment variable is defined at the workflow level for consistency and easier maintenance.

4. **Code Checkout**:  action is used to fetch the repository's code into the runner for both jobs.

5. **Secure Secrets**: Docker Hub credentials are stored as GitHub secrets and accessed securely within the workflow.

6. **Build caching**: Cahing is applied when building the application

7. **Optimized Docker Build**: Docker images are built and pushed using Docker actions, with caching utilized for dependencies, improving efficiency.