![Status badge](https://github.com/timur-harin/S24-core-course-labs/.github/workflows/flutter.yml/badge.svg)

# CI Best Practices

1. **Automate the Build**: Ensure that the build process is automated so that every code change triggers a build to catch issues early.

2. **Use Version Control**: Always use version control for your codebase to track changes and facilitate collaboration.

3. **Isolate Dependencies**: Use tools like Docker to isolate dependencies and ensure consistency across different environments.

4. **Run Tests**: Include automated tests in your CI pipeline to verify the code changes and catch regressions.

5. **Linting**: Integrate linters to enforce coding standards and maintain code quality.

6. **Parallelize Builds**: Speed up the build process by running tests and other tasks in parallel where possible.

7. **Monitor Performance**: Keep an eye on build times and performance metrics to optimize the CI pipeline.

8. **Security Scans**: Integrate security scans to detect vulnerabilities in dependencies and code.

9. **Incremental Builds**: Optimize your build process to only build and test what has changed to reduce build times.

10. **Feedback Loop**: Ensure that developers receive feedback on their changes quickly to encourage best practices and rapid iteration.

## Implemented

In the provided workflow:
1. **Branch Protection:** The workflow is triggered on `pull_request` events for the `main` branch and specific paths within the `app_flutter` directory, ensuring that the workflow runs for changes related to the Flutter application only.

2. **Environment Isolation:** Each job specifies the `runs-on: ubuntu-latest` to ensure consistency and reproducibility of the environment.

3. **Dependency Management:** The workflow includes steps to install dependencies using `flutter pub get` and manage Docker-related dependencies for building and pushing Docker images.

4. **Linting and Code Formatting:** Code linting is performed using `flutter format --set-exit-if-changed` to ensure consistent code style.

5. **Docker Image Build:** The workflow includes a step to build and push a Docker image for the Flutter application based on the specified Dockerfile and context.

6. **Secret Management:** Secrets for DockerHub login (`DOCKERHUB_USERNAME` and `DOCKERHUB_TOKEN`) are securely accessed using `${{ secrets.SECRET_NAME }}` syntax to prevent exposing sensitive information in the workflow file.