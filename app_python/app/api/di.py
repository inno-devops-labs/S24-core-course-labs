"""
Setup API dependency injections.
"""

from fastapi import Request

from app.domain.time import TimeManager


async def time_manager(request: Request) -> TimeManager:
    """Returns TimeManager"""
    return request.app.state.time_manager
