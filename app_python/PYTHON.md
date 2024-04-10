# Lab 1

---

## Task 1: Python Web Application

### Framework Selection

I chose `fastAPI` as a framework for python web application
because it allows creating simple API. Also, `FastAPI` is using
`pydantic` library to ensure type safety and converts request
data to Pydantic class automatically. In addition,
framework creates API documentation automatically from code.

---

## Task 2: Well Decorated Description

### Best Practices

1. API described and constructed dynamically from `api` folder internals.
   Currently, API to get time is in the following path: `api/v1/time`
   (Both in project and in API). It allows to add new functionality and
   new version API without changing other parts of API.

2. Additional information of API inside code
   (`tags` in `APIRouter`, `response_model` in `API`, etc.).
   This information allows `FastAPI` to describe API documentation.

### Testing

There are 3 unit tests for time api path testing:

- For correctness of response
- For correctness of sending type
- For correctness of time as some time passes

#### Testing Best Practices

- Configuration file in separate file to configure test env and isolating it from application
- Each Unit test is as small as possible
- Naming of test
  corresponds
  to [Descriptive and Meaningful Phrases (DAMP)](https://imsadra.me/unit-testing-in-python-and-best-practices#heading-5-damp-andamp-dry-principles-in-your-tests)
- Using conventional naming for test files
