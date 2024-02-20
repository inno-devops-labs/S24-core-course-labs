# CI

## Practices used

Most of the practices are reused from Python projects, see `../app_python/CI.md`

Some changes:
1. Dependency caching is done via setup-dotnet (see
   [link](https://github.com/actions/setup-dotnet?tab=readme-ov-file#caching-nuget-packages))
2. Run only on changes withing app_csharp folder