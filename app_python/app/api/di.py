"""
Setup API dependency injections.
"""

from fastapi import Request

from app.domain.time import TimeManager
from app.domain.visits import VisitsStorage


async def time_manager(request: Request) -> TimeManager:
    """Returns TimeManager"""
    return request.app.state.time_manager


async def visits_storage(requests: Request) -> VisitsStorage:
    """Returns VisitsStorage"""
    return requests.app.state.visits_storage
