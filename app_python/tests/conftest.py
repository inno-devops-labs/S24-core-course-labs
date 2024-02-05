plugins = ["time_manager"]
pytest_plugins = ["tests.plugins." + name for name in plugins]
