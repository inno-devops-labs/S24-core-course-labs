# CI Best Practices

## Specific Version Use
Explicit versions are used for all actions. This avoids issues with the latest version introducing breaking changes. For example, actions/setup-python@v2 and actions/cache@v2 are used, rather than just relying on the @v2 tag.

## Cache Dependencies
The actions/cache@v2 action is employed to cache Python dependencies. This technique greatly speeds up the execution times of workflows, as pip packages don't have to be downloaded every time a workflow runs.

## Secure Handling of Secrets
Sensitive information, such as Dockerhub credentials and Snyk tokens, are stored as secrets and referenced in workflows. This avoids directly storing sensitive information in version control and complicates unauthorized access.

## Running the Linter and Tests
A linter and test suite are run as part of the CI workflow. This ensures that all committed code meets the set styling standards (flake8), and that all tests (pytest) pass.

## Security Vulnerability Detection
The Snyk action is used to check for vulnerabilities, ensuring that the application does not contain known security issues.

## Docker Actions
The Docker Login and Docker Build & Push steps use the official Docker actions for logging into DockerHub and building and pushing Docker images respectively. This makes the build process smoother and more maintainable.

## Controlling the Execution Order of Jobs
The 'needs' keyword is employed to control the execution order of jobs. For the docker job to run, both the build-and-test and security jobs must successfully complete first. This introduces a level of dependency management ensuring the Docker image is only built when the code passes quality checks and vulnerability scans.