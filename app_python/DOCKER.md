# Docker

In this app, I implemented the following best practices:

- Build a rootless container: the app starts on behalf of `app`;
- Make executables owned by root;
- Use trusted base images: `python` in my case;
- Expose only necessary ports;
- Utilize layer caching (layer sanity).

I also used [hadolint] to lint my Dockerfile.

[hadolint]: https://hadolint.github.io/hadolint/
