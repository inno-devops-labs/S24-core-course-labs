"""
App config module
"""
from sanic import Config


class AppConfig(Config):
    """
    Sanic app config
    """
    NTP_SERVER = "time1.google.com"
    NTP_VERSION = 3
