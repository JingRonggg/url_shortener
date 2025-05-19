from fastapi import APIRouter

router = APIRouter(
    prefix="/url",
    tags=["url"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def read_root():
    return {"message": "URL router is working!"}
