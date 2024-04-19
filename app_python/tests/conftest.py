plugins = ["time_manager", "visits_storage"]
pytest_plugins = ["tests.plugins." + name for name in plugins]
