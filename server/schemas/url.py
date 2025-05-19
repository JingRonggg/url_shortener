from pydantic import BaseModel, Field


class URLBase(BaseModel):
    target_url: str = Field(
        ..., title="Target URL", description="The URL to be shortened."
    )
