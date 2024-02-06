# Project Description

## Framework Selection

For this project I used Rust actix-web because of the performance and safety guarantees. 


## Best Practices Followed

- The application is structured as a Rust crate, enhancing modularity,separation of responsibilities and preventing import errors.
- Application routing and business logic are separated into distinct modules for improved maintainability.
- Adherence to idiomatic rust coding style is strictly maintained.
- Unit tests are implemented to verify the application's functionality and robustness.
- A linter is utilized to maintain code quality across the project.
- Dependency management is facilitated through a `cargo.toml` file, ensuring a consistent development and deployment environment.
- Including observability, tracing and metrics

## Ensuring Best Practices, Testing and Code Quality
- `Rustfmt` is used as the code formatter to achieve consistent coding styles throughout the project.
- `clippy` is employed to identify potential code quality issues, ensuring adherence to best practices.
- `taupaline` is employed to to check for code coverage in the CI.
- Comprehensive tests for all utility functions and endpoints are written using the test module built into the rust standart library
- Logging using `QuickWit`, tracing using `Jaegar` and Visualizations using `Grafana`.
- Adding a CI to run on each push and pull request.

## Observability and Logging
[![QuickWit](https://i.postimg.cc/C5VCH645/image.png)](https://postimg.cc/ygvS7jtC)
[![Jaegar](https://i.postimg.cc/9X6X1HTJ/image.png)](https://postimg.cc/vDvdHj0V)
[![Grafana](https://i.postimg.cc/63KLCmc3/image.png)](https://postimg.cc/FfPL4G25)