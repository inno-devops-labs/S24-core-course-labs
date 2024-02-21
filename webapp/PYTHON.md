# Django Framework

## Why

For this assignment particularly, using Django is a bit overcomplicated way, because we can use less code and time and do it with Flask, for example. But I decided to choose django because I use Django in my work, and it will be easier for me to do next assignments.

## In addition

It would be easier for me to use Django is really powerful framework with a lot of features, such as Django ORM, Django REST technology for APIs.

## About the app itself(best practices)

### 1. MVC
Django use MVC design pattern, like the most part of the frameworks. So, for the time I created a new app "msk_time", which has a view that contains a View class with get method that returns a JSON with current Moscow time.

# Unit Tests

## Unit tests overview

Unit tests have been created to verify the functionality and behavior of various components within the Django application. These tests cover views for now to ensure that individual units of code work as expected.

## Best Practices Employed

### 1. Test Organization

Unit tests are organized into separate modules based on the components they are testing. For example, models, views, forms, and utility functions each have their own test module within the tests package.

### 2. Test Naming Convention

Test case names are descriptive and follow a consistent naming convention to clearly indicate what aspect of the component is being tested. For example, test methods are prefixed with test_ followed by a brief description of the test scenario.

### 3. Use of Assertions

Assertions are used to verify the expected behavior of the code being tested. Common assertions such as assertEqual, assertTrue, and assertFalse are used to validate the results of function calls, form validations, and other conditions.

## Unit Tests Description

### Views

Tests have been written to validate the functionality of Django views. These tests simulate HTTP requests and verify that the views return the expected responses, handle input data correctly, and handle errors appropriately.