![Status badge](https://github.com/timur-harin/S24-core-course-labs/.github/workflows/python.yml/badge.svg)

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
In the provided workflow, the following best practices were implemented:

1. **Branch Protection:** The workflow is triggered on `push` and `pull_request` events for the `main` branch, ensuring that the workflow runs for changes to the main branch only.
   
2. **Environment Isolation:** Each job specifies the `runs-on: ubuntu-latest` to ensure consistency and reproducibility of the environment.

3. **Dependency Caching:** Caching is used for dependencies to speed up the workflow by avoiding redundant installations. Dependencies like `pip`, `poetry`, and `Snyk` dependencies are cached using the `actions/cache@v2` action.

4. **Secret Management:** Secrets like `DOCKERHUB_USERNAME`, `DOCKERHUB_TOKEN`, and `SNYK_TOKEN` are appropriately used with the `${{ secrets.SECRET_NAME }}` syntax to avoid exposing sensitive information in the workflow file.

5. **Code Quality Checks:** The workflow includes linting and vulnerability checks using tools like `flake8` and `Snyk` to maintain code quality and security.

6. **Code Testing:** Automated tests are run using `pytest` to ensure code functionality.

7. **Modular Steps:** The workflow is organized into different jobs (`install_clear_test_lint`, `docker`, `snyk`), each responsible for a specific set of tasks, promoting modularity and maintainability.