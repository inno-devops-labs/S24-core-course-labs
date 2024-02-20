# Best pratices used for CI

1. Caching

We are using a caching for a Poetry in order to save time on dependencies installing if we trigger the workflow several times.

2. Specific hash for Actions versions

We are using specific hashs for Actions versions in order to be sure that the behaviour of our workflow won't change due to bad commits in Actions repositories.

3. Specific runner version

We are using specific runner versions in order to be sure that the behaviour of our workflow won't change due to bad changes in `latest` runner.

4. `if` statement

We are skipping a `push` part since we do not want to update the image every time we push to the branch.

We can do it using `if`, where we specified that pushing is done if and only if we push (merge in fact) to the main.
