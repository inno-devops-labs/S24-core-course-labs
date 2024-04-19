"""Service handlers (addons)."""

from fastapi import APIRouter, Depends, responses

from app.api import di
from app.domain.visits import VisitsStorage

router = APIRouter()


@router.get("/health")
async def health():
    """Health handler."""
    return {"status": "ok"}


@router.get("/visits", response_class=responses.JSONResponse)
async def show_time(
    visits_storage: VisitsStorage = Depends(di.visits_storage),
):  # noqa: E251
    """Returns number of times app was accessed."""
    visits = await visits_storage.read_data()
    return responses.JSONResponse(content={"visits": visits})
