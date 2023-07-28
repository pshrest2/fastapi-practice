from fastapi import FastAPI, Depends
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()

items_db = [{"name": "Foo"}, {"name": "Bar"}, {"name": "Baz"}]


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class CommonQueryParams:
    def __init__(self, q: str | None = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit


@app.get("/items")
async def get_items(commons: Annotated[CommonQueryParams, Depends(CommonQueryParams)]):
    res = {}
    if commons.q:
        res.update({"q": commons.q})
    items = items_db[commons.skip : commons.skip + commons.limit]
    res.update({"items": items})
    return res


@app.post("/items")
async def create_item(item: Item):
    return item


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.model_dump()}
