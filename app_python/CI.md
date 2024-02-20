# CI Description


A CI workflow is defined within the `.github/workflows/ci_python.yaml file`, designed to perform several key tasks: linting and testing the application, conducting code vulnerability assessments via SNYK, and building and pushing a Docker image. This workflow is initiated exclusively upon modifications to the app_python directory or the workflow file itself.

The workflow operates on an `ubuntu-22.04` runner, utilizing `Python 3.9`.

Where possible, the workflow employs official actions. However, for the security task, custom actions were necessary because SNYK's requirement for the project to be located in the root directory conflicts with the project's placement in the `app_python` directory.


## Jobs Overview
The workflow comprises three distinct jobs:

- Build: This job handles linting and testing the application. Even if linting fails, the job proceeds to application testing. A failure in the testing phase will result in the job's failure.
- Security: This job performs a vulnerability check using SNYK. The workflow halts if this job fails, which occurs only when a vulnerability of high or critical severity is detected.
- Docker: This job is responsible for building and pushing the Docker image to Docker Hub, contingent upon the success of preceding jobs. It proceeds only if all tests are passed and no significant vulnerabilities are identified.

## Best Practices

- Workflow activation is strictly tied to changes within the app_python directory or the workflow file, minimizing unnecessary runs.
- To enhance efficiency, caching strategies are implemented. For instance, the build job caches Python packages to circumvent repeated downloads during `pip install`-  executions. Similarly, the Snyk CLI tool is cached to streamline the security job.
- The workflow is optimized for early failure detection, with tests being prioritized to quickly halt the process in case of failures.
- An emphasis on parallel job execution (e.g., build and security jobs running concurrently) optimizes time and resource usage. The Docker job, however, is sequentially executed to ensure Docker images are built and pushed only after successful test and security checks.
- Jobs are bounded by time limits to ensure efficiency.
- Explicit declarations of OS and Python versions in the workflow file ensure a controlled and predictable execution environment.
- Use of repository secrets and no credentials hardcoded in the workflow configurations