# CI best practices
For my implementation I followed the following practices:
* specified workflow trigger: since workflow should be triggered only when `app_python` or workflow file itself changed, I set trigger condition only for two cases to avoid useless runs;
* set timeouts: to avoid infinite runs, I restricted execution time by setting timeouts;
* specified python version: 3.10;
* specified OS version: `ubuntu-22.04`;
* caching: caching `pip` to not download dependencies several time, it saves time; 
* fails as fast as it can: I put stop-point where it is necessary, for example, workflow cannot continue if tests fail (from common knowledge), it makes programmer save time in error/fail cases;
* runs jobs in parallel: `build` and `security` jobs run in parallel since they do not depend on each other to save time, however, `docker` job cannot be done if some of previous jobs fails.

Following these practices, my workflow began secure, fast and reliable.