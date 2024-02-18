# CI Workflow Documentation

This document provides an overview of the Continuous Integration (CI) workflow implemented in this project. The workflow
is defined in the `.github/workflows/ci.yml` file.

## Workflow Status Badge

![CI](https://github.com/hermandyudin/S24-core-course-labs/workflows/CI/badge.svg)

Click on the badge to view the details of the CI workflow.

## Best Practices Implemented

### 1. Parallelism

The CI workflow utilizes parallel steps to speed up the build process by executing multiple tasks simultaneously.

### 2. Caching

Dependencies are cached to reduce build times. The caching strategy is based on the hash of the `requirements.txt` file.

### 3. Matrix Builds

The workflow supports multiple versions of Python by using a matrix build. It tests the code against different Python
versions.

## Snyk Vulnerability Checks

The workflow includes Snyk vulnerability checks to identify and address potential security vulnerabilities in the
project.

## Build Cache

The build cache is utilized to enhance workflow efficiency, preventing unnecessary reinstallation of dependencies.