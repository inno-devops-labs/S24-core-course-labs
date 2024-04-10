"""
App config module
"""
import os

from sanic import Config


class AppConfig(Config):
    """
    Sanic app config
    """
    NTP_SERVER = "time1.google.com"
    NTP_VERSION = 3
    COUNTER_FILE = f"{os.environ['VISITS_PATH']}/{os.environ['VISITS_FILE']}"
