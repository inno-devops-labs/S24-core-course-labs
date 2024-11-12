# CI Best practices

The GitHub Action Workflow utilizes some of the best CI practices:

* The secrets are stored securely and not exposed through the github action workflow
* The workflow utilizes build caches to speed up subsequent CI executions.

Unfortunately integrating Snyk into the Workflow was not possible due to its unavailability in Russia.

