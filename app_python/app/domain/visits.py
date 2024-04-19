from abc import ABC, abstractmethod
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class VisitsStorageConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env.visits")


class VisitsFileStorageConfig(VisitsStorageConfig):
    file_path: Path = Path("visits")
    encoding: str = "utf-8"


class VisitsStorage(ABC):
    @abstractmethod
    def __init__(self, config: VisitsStorageConfig): ...

    @abstractmethod
    async def read_data(self) -> int: ...

    @abstractmethod
    async def increment_data(self) -> None: ...


class VisitsFileStorage(VisitsStorage):
    def __init__(self, config: VisitsFileStorageConfig):
        self.file = config.file_path
        self._encoding = config.encoding

        self.file_mount()

    def file_mount(self):
        if self.file.exists():
            return

        with open(self.file, "w", encoding=self._encoding) as file:
            file.write(str(0))

    async def read_data(self) -> int:
        with open(self.file, "r", encoding=self._encoding) as file:
            return int(file.read())

    async def increment_data(self) -> None:
        with open(self.file, "r+", encoding=self._encoding) as file:
            visits = int(file.read() or "0")
            visits += 1

            file.seek(0)
            file.write(str(visits))
