# CI Best Practices

- **_Dependency Installation_**: Ensure project dependencies are installed using `pip` from the `requirements.txt`.

- **_Code Quality Checks_**: Perform code linting using tools to enforce code style standarts.

- **_Vulnerability Security_**: Integrate Snyk into the CI workflow to identify and address vulnerabilities.

- **_Security_**: Avoid hardcoding sensitive information, such as access tokens, passwords, and API keys, directly into
  code or configuration files.

- **_Trigger Conditions_**: Configure the workflow to trigger on pushes, ensuring that changes are validated before
  merging.

- **_CI Badge_**: I use CI badge to visually display the current status of my CI workflows.

- **_Docker Build_**: Build Docker images and push them to Docker Hub for versioning and deployment.