# Python description

## Framework

As production-ready framework I use FastAPI version 0.103.1

### Pros of FastAPI:

1) Ease to use: FastAPI has very clear and straightforward design. It is user-friendly and can be studied pretty fast
2) Performance: FastAPI is optimized with Python type hint and has some automatic features like data validation and serialization, which grants fast performance
3) Integration of features: FastAPI has on opportunity to integrate a lot of features like authentication, API routing, input validation, request handling, dependency injection and other
4) Scalability: FastAPI is build on top of asynchronous web framework so can be used to build scalable applications or microservices. Also, with power of asyncio it can handle concurrent requests efficiently

### Cons of FastAPI:

1) Learning curve: to get familiar with framework there is really nothing to do and first application can be written within half of an hour. However, to get perfect knowledge it can take more time compared to other Python frameworks. This is due to its extensive features and use of asynchronous programming
2) Young project: FastAPI is relatively newer framework compared to others like Flask or Django, so its base of plugins and extensions is not so reach, however it is developing
3) Python compatibility: FastAPI relies on the async features introduced in Python 3.7, so it can not be compatible with older versions

Overall, I choose this framework because it can be easily scaled (which is crucial in context when we do not how our application will look at the end and new requirements come during development), has a great performance, and finally I have experience with it.

## Best practices applied:

1) Consistent & predictable project structure: all domains are stored in src folder, each package has its own FastAPI Router (also it has its own schemas, models, services etc. but at current moment there is no need in them)
2) Use Pydantic as data validator (at this moment no need in it)
3) Follow the REST
4) Docs: write docs for endpoints (there is no response model at current time)
5) Use type hints: FastAPI, Pydantic, and modern IDEs encourage to take use of type hints


## Tests

For tests I use pytest library. In this application, it hard to write complex tests, so I just test two routes: valid and invalid

### Best practices for unit tests

* Use TestClient from FastAPI: it is recommended to use TestClient, as it does nor rely on infrastructure, and we do not need to make direct requests to server
* Fixtures: for common test cases use predefined test data
* Test edge cases
* Test classes: for big number of tests it is better to organize them using test classes
* Independent tests: tests should run independently and do not rely on each other
* Include both positive and negative tests: it is important to check not only for expected behavior, but also for edge cases that may cause errors