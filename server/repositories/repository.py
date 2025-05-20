from typing import TypeVar, Generic
from pydantic import BaseModel


T = TypeVar("T")


class Repository(BaseModel, Generic[T]):
    def __init__(self, db):
        self.db = db

    async def get_all(self):
        return self.db.get_all()

    async def get_by_id(self, id):
        return self.db.get_by_id(id)

    async def create(self, data):
        return self.db.create(data)

    async def update(self, id, data):
        return self.db.update(id, data)

    async def delete(self, id):
        return self.db.delete(id)
