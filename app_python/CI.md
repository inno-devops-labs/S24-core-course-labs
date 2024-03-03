# Continuous Integration (CI) Workflow

The CI workflow is available in the `.github/workflows` directory. It's configured to run on every push. 

The CI workflow implements the following steps:
- Dependencies: Install the required dependencies.
- Linter: Run the linter to check for any linting issues.
- Tests: Run the unit tests to ensure the application is functioning as expected.
- Cache: Utilize build cache to enhance workflow efficiency.
- Docker: Login, build, and push the Docker image to Docker Hub.

Best practices
The CI workflow also includes a workflow status badge in the `README.md` file for visibility. Additionally, the CI workflow has been optimized by utilizing build cache to enhance workflow efficiency.

