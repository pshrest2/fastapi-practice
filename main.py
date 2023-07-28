from fastapi import FastAPI
from enum import Enum

app = FastAPI()

items = [{"name": "Foo"}, {"name": "Bar"}, {"name": "Baz"}]


@app.get("/items/{item_id}")
async def read_items(item_id: int, q: str | None = None):
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id": item_id}
