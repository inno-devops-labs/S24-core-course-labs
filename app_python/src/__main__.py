import uvicorn

from .config import config

if __name__ == "__main__":
    uvicorn.run("src.app:app", host=config.host, port=config.port, reload=True)
