from app.domain.time import TimeManager
from fastapi import Request


async def time_manager(request: Request) -> TimeManager:
    return request.app.state.time_manager
