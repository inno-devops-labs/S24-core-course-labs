import datetime
import typing as t

import pytz
from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class TimeManagerConfig(BaseSettings, case_sensitive=False):
    model_config = SettingsConfigDict(env_file=".env")

    dump_format: str = "%H:%M:%S %d.%m.%Y"
    timezone: t.Union[pytz.BaseTzInfo, str] = pytz.timezone("Europe/Moscow")

    @field_validator("timezone")
    @classmethod
    def _timezone(cls, v: t.Union[str, pytz.BaseTzInfo]):
        return pytz.timezone(v) if type(v) is str else v


class TimeManager:
    def __init__(self, config: TimeManagerConfig):
        self._dump_format = config.dump_format
        self._timezone = config.timezone

    async def datetime(self) -> datetime.datetime:
        return datetime.datetime.now(tz=self._timezone)  # type: ignore

    async def str_datetime(self) -> str:
        return (await self.datetime()).strftime(self._dump_format)
