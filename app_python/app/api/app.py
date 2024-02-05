"""
Web app setup
"""

import typing as t

from app.api.time import router as time_router
from app.domain.time import TimeManager, TimeManagerConfig
from fastapi import FastAPI


def create_start_app_handler(
    app: FastAPI
) -> t.Callable[[], t.Coroutine[None, None, None]]:
    """On startup event function"""
    async def start_app() -> None:
        time_manager_config = TimeManagerConfig()

        time_manager = TimeManager(time_manager_config)
        app.state.time_manager = time_manager

    return start_app


def get_application() -> FastAPI:
    """Get FastAPI web application"""
    application = FastAPI(
        title='DevOps Labs',
        version='1.0',
    )

    application.add_event_handler(
        'startup', create_start_app_handler(application)
    )
    application.include_router(time_router)

    return application
