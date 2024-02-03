# Copy of .git/hooks/pre-commit
black app_python
mypy app_python
pylint app_python
python -m unittest app_python.test

bun test app_bun
cd app_bun && bun run prettier . --write && cd ..
