## Justification for using Flask as the framework ##

The Flask framework was chosen for this Python web application due to the following reasons:

1. **Simplicity.** It is easy to set up and get started with minimal configuration. It provides an intuitive API for building web applications.
2. **Beginner-friendly.** It offers a documentation with explicit instructions.

## Best practises applied in web application ##

1. **Right tech stack chosen.** The Flask framework was chosen for this application due to the best correspondence between funcctionality of a framework and the application requirements.
2. **The code is keep concise** The code for the application is easy readable and follows coding standards.

## Explanation on following coding standards, implementing testing, and ensuring code quality ##

**Following coding standards.** he code follows PEP 8 guidelines, which are the standard Python style guide. This includes consistent indentation, proper naming conventions, and appropriate code formatting.
**Testing**. The testing was implemented by continuous monitoring.
**Code quality.** The code quality ensured by following coding standards and debugger using.

## Unit tests ##

1. The `test_index_status` function tests if the status code of making a GET request to the root endpoint is 200, which indicates that the endpoint is reachable and responding correctly.

2. The `test_msc_time_format` function tests if the response from the `msc_time` function follows the 'YYYY-MM-DD HH:MM:SS' format by checking the length of the response and the positions of the hyphens, spaces, and colons in the string.

3. The `test_msc_time_response` function tests if the response from the `msc_time` function is split correctly into date and time components, each of the correct length after splitting.

### Best practices for testing in this scenario include: 

1. Isolation of tests: Each test is independent and self-contained, not relying on shared state across tests. This helps maintain test reliability and makes it easier to pinpoint failures.
2. Meaningful test names: Used descriptive test names that clearly indicate what is being tested to enhance readability and understanding.
3. Mocking dependencies: Used mocking frameworks or techniques to isolate the unit under test from external dependencies that are not relevant for the specific test case.
4. Tests kept simple and focused: Each test focus on a specific aspect of the function or component being tested. Complex tests combining multiple functionalities are avoided.

## CI workflow 

This repository uses GitHub Actions to automate the testing and building. 
### Steps included in workflow are: 
1. Set up Python:
   - Checks out the code
   - Sets up the Python environment with the specified version
   - Caches the dependencies to speed up future builds
   - Installs the necessary dependencies using pip
   - Lints the code using flake8 to identify syntax errors and undefined names
   - Tests the code using pytest

2. Set up QEMU:
   - Configures QEMU, an open-source machine emulator and virtualizer, for use in the build process

3. Set up Docker Buildx:
   - Sets up Docker Buildx, a Docker CLI plugin that extends the capabilities of the Docker command-line tool

4. Login to Docker Hub:
   - Uses Docker login action to log in to Docker Hub with the specified credentials

5. Build and push:
   - Builds the Docker image for the Python application
   - Pushes the built image to Docker Hub with the specified tags

### Best practices for CI applied 

1. **Used Matrix Strategy**: Used the matrix strategy to define the version range. Used `strategy.matrix` key in the workflow. It is containing one version by now, but can be easily expanded.
2. **Cache Dependencies**: Used Cache Python dependencies to speed up the workflow execution by storing them in between workflow runs.
3. **Separate Test and Build Steps**: The linting, testing, and building steps are split into separate jobs within the same workflow.