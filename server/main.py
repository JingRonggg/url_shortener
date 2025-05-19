from fastapi import FastAPI
from server.routers import url_routers

app = FastAPI()

app.include_router(url_routers.router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
