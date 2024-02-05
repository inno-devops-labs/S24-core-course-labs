# Moscow time application

## Framework choice justification
I used the built-in ```http.server``` package. It is appropriately minimal, and does not require any external dependencies.

## Best practices
- The application is set up as a module.
- Code adheres to PEP standards and pylint
- Virtual environment can be utilised for development

## Ensuring code quality
- ```make lint``` may be utilised to run ```pylint``` and PEP checks on the project.
- Pre-commit integration added for ```pylint```, ```black```, trailing whitespace and EOF fixers.
