## Best practices in Continuous Integration .yaml file

1. **Chaching mechanism usage**

To speed up the process of building, I'm using chaching of previously downloaded requirements.

2. **Sequence of jobs**

First of all, there is checking code by linting, testing and looking for vulnerabilities, only then push new docker image to the DockerHub.

3. **Secured credentials**

Using GitHub secrets in CI configuration file to ensure security of sensitive information. 

4. **Granulated structure**

Each step is separated and has its own identificator `name`, so the configuration content is easily navigated.

5. **Vulnerability scanning**

Usage of Snyk implies effective searching for project vulnerabilities. In case they are present, this will allow to notice and eradicate them quickly.

6. **Relevant actions version**

Usage of non-deprecated actinos versions.