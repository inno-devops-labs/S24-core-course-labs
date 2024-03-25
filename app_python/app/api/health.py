from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health():
    """Health handler."""
    return {"status": "ok"}
