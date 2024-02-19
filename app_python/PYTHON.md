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

Testing performed by using `pytest` and `pytest-time` for `time.sleep()`.
Test is written in a way that time requested from webapp two times
with 10 seconds pause. Then compare time after pause with calculated predicted time.