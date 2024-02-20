# CI

In this app's workflow, I implemented these best practices:

- Use secrets for confidential data (Docker Hub's token);
- Set a custom timeout for jobs (I set it to 15 minutes since the build takes
  some time);
- Use only trusted actions;
- Use caching.
