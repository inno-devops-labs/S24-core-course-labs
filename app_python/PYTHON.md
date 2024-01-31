# Framework

FastAPI was chosen for this lab.

It has very high performance as it is based on Starlette and Pydantic.

FastAPI takes advantage of standard Python type declarations in function parameters to declare request parameters and
bodies, perform data conversion (serialization, parsing), data validation, and automatic API documentation with OpenAPI
3 (including JSON Schema).

It includes tools and utilities for security and authentication (including OAuth2 with JWT tokens), a dependency
injection system, automatic generation of interactive API documentation, and other features.

## Best practices

- Separate static file serving routes from api routes
- The server can accept any timezone, but the client uses only a specified one. It makes the solution extendable, if
  needed.
- Validate given timezone and throw **400 Bad Request** with the message to explain the error.