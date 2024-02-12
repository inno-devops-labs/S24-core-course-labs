# Framework & Best Practices

## Justification for Actix Web framework

I have chosen the Actix Web framework for the following reasons:

- Type Safety: Actix Web is built on top of Actix, a powerful actor framework.
  It is designed to be type-safe and to prevent common errors at compile time.

- Feature Rich: Actix provides a lot of features out of box. HTTP/2, logging,
  etc.

- Extensibility: one can easily create their own libraries that any Actix
  application can use.

- Performance: Actix is blazingly fast. It is one of the fastest web frameworks
  available according to the [TechEmpower benchmarks][tech-empower-benchmarks].

[tech-empower-benchmarks]: https://www.techempower.com/benchmarks/#section=data-r21&hw=ph&test=fortune

## Best Practices

To ensure code quality and maintainability, I have applied the following best
practices to my web application:

- Used the `rustfmt` code formatter to enforce consistent code style and
  formatting according to the Rust style guide.

- Used `clippy` to catch common mistakes and improve my code. Moreover, I
  thoroughly configured clippy to enforce stricter rules.

- Installed `pre-commit` hooks to automatically run code formatting, linting,
  and testing.

- Utilized the `cargo` package manager for dependency management.

- Utilized `.gitignore` to keep the repository clean.

These practices help in maintaining clean and readable code, improving code
quickly develop APIs.

## Unit Testing

Since Actix Web provides tools to perform integration tests against your
applications and unit test tools for custom extractors and middleware. I have
written tests for the following:

1. **Test success path (test_get_returns_success)**: The test asserts that the
   endpoint returns `200`.

1. **Time Equality Test (test_time_is_equal)**: The test asserts that the time
   returned by the API is the same as the current time in Moscow.
