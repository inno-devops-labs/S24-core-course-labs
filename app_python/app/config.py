"""
Config for setup app.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


# pylint: disable=C0115, R0903
class Config(BaseSettings, case_sensitive=False):
    model_config = SettingsConfigDict(env_file=".env")
