# Lab 1.
## Task 1;
Reasons for choosing the Flask framework:
- I have no experience working with python frameworks. I only know that there are 3 main ones: Django, Flask, and Pyramid. Of the above, it seemed to me that Flask is the most native and simple.
- Nevertheless, I already had a little experience working with Flask, where I prescribed endpoints for a server application.
Summarizing all the above, I chose Flask as the main framework for the application.

## Task 2;
## Best practices/coding standards used in this web application:
- It uses a ready-made framework for creating service endpoints and working with them, rather than self-written interactions with sockets directly.
- Using .gitignore file in order not to transfer unnecessary/confidential information to the repository
- Storing environment variables in .env .This will allow you to change them or dynamically change them in the future with CI/CD
- Using a docker container. There is a docker file in the directory that should be used to start the server.
- I wrote unit test for this simple python program (`test_app.py`)