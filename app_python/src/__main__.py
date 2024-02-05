import uvicorn

from app_python.src.config import config

if __name__ == "__main__":
    uvicorn.run("app_python.src.app:app", host=config.host, port=config.port, reload=True)