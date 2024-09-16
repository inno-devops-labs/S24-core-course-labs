## Selected framework 
I have chosen Flask as the framework for my web application due to several reasons:

1. *Simplicity and Flexibility*: Flask is a micro web framework for Python. It doesn't come with additional tools and libraries like Django, which makes it a lot simpler and flexible. You have the freedom to choose your own tools and libraries according to your project needs.
2. *Built for Speed and Scalability*: Flask allows developers to create lightweight and efficient web apps which are fast and scalable.
3. *Great community support*: Flask has an active community and good support for problem-solving. The probability of getting stuck is less as someone might have already faced a similar issue before.

## Best practices 
I have used several best practices in my implementation:

1. *Coding standards and quality*: I followed the PEP8 standard in my implementation to keep my code clean and to make it easy for other developers to read also I used linter.
2. *Requirements*: My project folder contains *requirements.txt* that contains all necessary libraries to run the application.
3. *Tests*: I have implemented test that checks that site is working and working correctly.
4. *Logging*: I collect logs about usage of my app.
5. *Error handling*: The user will see the error page if error happened. 
6. *Code documentation*: The code is documented using comments to improve the understanding of the person who just came across my implementation of what the function does.

## Testing
Test was implemented using `pytest`. One test is like ping, other checks that time is correct.

## Code Quality
As was said, I used `pylint` and PEP8 standard for `python` code