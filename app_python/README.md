# Moscow Time Web Application

## Overview

This web application, built using Flask, displays the current Moscow time on a webpage. It utilizes HTML templates for rendering and dynamically updates the time using JavaScript.

## Table of Contents

- [Getting Started](#getting-started)
  - [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Running Tests](#running-tests)
- [Technologies Used](#technologies-used)

## Getting Started

### Prerequisites

- Python 3.x
- Pip (Python package installer)

### Installation


1. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Project Structure

```plaintext
app_python/
|-- application.py
|-- test_application.py
|-- static/
|   `-- moscow.jpg
`-- templates/
    `-- current_time.html
```
*   **application.py:** Main application file containing Flask code.
*   **test\_application.py:** Test file ensuring the correctness of the application's functionality.
*   **static/:** Directory for static files, such as images.
*   **templates/:** Directory for storing HTML templates.

Usage
-----

To run the web application, execute the following command:

bashCopy code

`python application.py`

Visit `http://127.0.0.1:5000/` in your web browser.

Running Tests
-------------

To run tests, execute the following command:

bashCopy code

`python test_application.py`

Technologies Used
-----------------

*   Flask
*   Jinja2
*   HTML

