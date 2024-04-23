from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="",
    tags=["meta"])


class VisitsResponse(BaseModel):
    visits: int


@router.get(
    path="/visits",
    responses={200: {"description": "Success"}})
def get_current_time_in_msk_timezone() -> VisitsResponse:
    try:
        return VisitsResponse(visits=int(open("visits").read()))
    except FileNotFoundError:
        return VisitsResponse(visits=0)
