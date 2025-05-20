from fastapi import APIRouter

router = APIRouter(
    prefix="/url",
    tags=["url"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_urls():
    """
    Get all URLs.
    """
    return {"message": "Get all URLs"}


@router.get("/{url_id}")
async def get_url(url_id: int):
    """
    Get a shortened URL by URL.
    """
    return {"message": f"Get URL with ID {url_id}"}


@router.post("/")
async def create_url(url: str):
    """
    Create a new shortned URL.
    Return shortened URL.
    """
    return {"message": f"Create URL {url}"}


@router.put("/{url_id}")
async def update_url(url_id: int, url: str):
    """
    Update a shortened URL by URL.
    Return updated shortened URL.
    """
    return {"message": f"Update URL with ID {url_id} to {url}"}


@router.delete("/{url_id}")
async def delete_url(url_id: int):
    """
    Delete a URL by ID.
    """
    return {"message": f"Delete URL with ID {url_id}"}
