# CI

## Best Practices

1. **Leveraging GitHub Actions Marketplace**: A number of already developed
   actions are used to enhance both development time and security
2. **Handling Secrets Safely**: All the secrets are stored using GitHub's
   special feature for that
3. **Concurrent Workflow Management**: Only when python application changes the
   workflow is triggered which helps to utilize resources more efficiently
4. **Caching**: the build workflow uses caches to decrease resource usage and
   make builds faster
