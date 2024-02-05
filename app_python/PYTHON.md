# Python Web Application

## Justification for Using Flask Framework

To develop a simple Python web application for displaying
the current time in Moscow, I chose the Flask framework.

Flask is a lightweight and flexible web framework that
is well-suited for small to medium-sized projects. The decision
to use Flask for this specific application is based on several factors.

### Simplicity and Minimalism

Flask is known for its simplicity and minimalism.
It provides just what is needed for building web applications
without unnecessary complexity. Given the straightforward nature of
the task – displaying the current time in Moscow – Flask allows
for a concise and easy-to-understand implementation without
additional overhead.

```python
from flask import Flask
import time

app = Flask(__name__)

# ... (Implementation)
```

### Quick Setup and Deployment

Flask offers a quick and easy setup process.
With just a few lines of code, a basic web application can be created.
This simplicity is beneficial for rapid development and deployment,
making it an ideal choice for small projects or prototypes.

```python
if __name__ == '__main__':
    app.run(debug=True)
```

### Routing and URL Handling

Flask's routing system is intuitive and allows for easy definition
of endpoints. In this application, the route '/' is defined to display
the current time in Moscow. This makes the code organized and readable.

```python
@app.route('/')
def display_moscow_time():
    moscow_time = get_moscow_time()
    return f"Current time in Moscow: {moscow_time}"
```

### Flexibility and Extensibility

While Flask is lightweight, it provides flexibility and can be extended
as needed. This flexibility makes it adaptable for a wide range of
projects, including small applications like the one being developed here.

### Conclusion

Considering the simplicity of the task, the need for quick development,
and the minimalistic nature of the application, Flask emerges as a
suitable choice. It allows for a clean and straightforward
implementation, making the development process efficient and the
codebase easy to maintain.

## Best Practises

I used `pytz` and `datetime` libraries because It's generally
recommended to use such modules for accurate
and reliable time zone handling

I used <https://www.pythonchecker.com/> with PEP8 style guide for Python
and got `72%` of code quality which considered as `Very Good`
