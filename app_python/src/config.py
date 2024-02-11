import os


class Config:
    host = os.getenv("SERVER_HOST", default="0.0.0.0")
    port = int(os.getenv("SERVER_PORT", default=8080))


config = Config()
