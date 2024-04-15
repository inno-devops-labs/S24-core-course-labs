# CI Workflow Best Practices

This document outlines the best practices implemented in the CI workflow of our project. These practices help improve the efficiency, reliability, and security of our CI process

## Workflow Status Badge

We have added a workflow status badge to provide visibility into the status of our CI workflow. The badge indicates whether the workflow is passing or failing. Here's the markdown used to display the badge:

[![CI](https://github.com/hugowea/S24-core-course-labs/actions/workflows/ci.yml/badge.svg)](https://github.com/hugowea/S24-core-course-labs/actions/workflows/ci.yml)

## Optimization

We have optimized our CI workflow using the following strategies:

### 1. Build Cache

To enhance workflow efficiency, we utilize build caching. This helps avoid re-downloading and re-installing dependencies that haven't changed since the last successful workflow run.

### 2. Parallelization

We have parallelized our tests to run them concurrently, reducing the overall test execution time.

### 3. Dependency Management

We use a dependency management system to manage our project's dependencies. This ensures consistent and reproducible builds.

## Snyk Vulnerability Checks

We have integrated Snyk into our CI workflow to identify and address vulnerabilities in our projects. The following steps were taken to implement Snyk vulnerability checks:

We added the Snyk CLI tool to our workflow to scan our project for vulnerabilities.

The Snyk vulnerability scan is performed in parallel to build.

The Snyk scan results are displayed in the workflow log, and appropriate actions are taken to address any identified vulnerabilities.

## Conclusion

By following these best practices and integrating Snyk vulnerability checks into our CI workflow, we ensure that our project is built efficiently, tested thoroughly, and vulnerabilities are addressed promptly.
