# Copy of .git/hooks/pre-commit
black app_python
mypy app_python
pylint app_python
pytest ./app_python/test_app.py
