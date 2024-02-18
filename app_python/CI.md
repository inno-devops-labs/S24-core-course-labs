## Best practices applied to CI workflow

1. **Set timeouts** - to avoid endless jobs (because of deadlocks or something like this) need timeouts to be specified: job will be killed immediately after timeout exceeds

2. **Use well-known actions in your workflow** - actions are close to dependencies in sense of security and stability

3. **Limit scope for tokens inside workflows** - usually tokens has wide-range of permissions, however not every job need all privileges to be completed. So it is good to provide only essential rights

4. **Cache steps and jobs if possible** - caching optimizes time of jobs to be completed, so long steps like deps downloading or docker build should be cached

5. **Accessing credentials** - Use GitHub secrets to store sensitive information for jobs without threat of revealing or hard-coding them

6. **Trigger WorkFlow only if related files was changed** - there is no need to rerun workflow if nothing in it was changed even if somebody has make any changes in repo (f.e no need to rerun app_python workflow if somebody want to make changes in README file)

7. **Setup jobs dependencies** - no need to build and publish docker image if test stage was failed, so need to create job dependent of another jobs that are essential to be successful for the current run