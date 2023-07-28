from fastapi import FastAPI
from enum import Enum

app = FastAPI()

items = [{"name": "Foo"}, {"name": "Bar"}, {"name": "Baz"}]


@app.get("/items")
async def read_items(skip: int = 0, limit: int = 0):
    return items[skip : skip + limit]
