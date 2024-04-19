from abc import ABC, abstractmethod
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class VisitsStorageConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env.visits")


class VisitsFileStorageConfig(VisitsStorageConfig):
    file_path: Path = Path("app_data/visits")


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

        self.file_mount()

    def file_mount(self):
        if self.file.exists():
            return

        self.file.write_text(str(0))

    async def read_data(self) -> int:
        with open(self.file) as file:
            return int(file.read())

    async def increment_data(self) -> None:
        with open(self.file, "r+") as file:
            visits = int(file.read() or "0")
            visits += 1

            file.seek(0)
            file.write(str(visits))
