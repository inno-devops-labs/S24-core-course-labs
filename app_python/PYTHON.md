# Python Moscow Time Web Application

## Overview
A simple Python Web Application that shows Moscow Time from any timezone

## Framework choice
I chose Python FastAPI Web framework for this project.

FastAPI
- suits perfectly for small projects
- have impressive performance
- no boilerplate
- quickstart & easy to use

## Best Practices
This project
- follows python consice PEP8 (naming conventions, comments and overall python code style)
- has unit tests
- github actions with pytest and flake8 

## Tests
Unit tests are written using `pytest` testing framework

All unit tests are located in `tests/unit` folder

On every `push` and `pull_request` gh action runs Pytest and flake8 with various python versions
