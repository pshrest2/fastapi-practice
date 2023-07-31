from pydantic import BaseModel
from fastapi import APIRouter, Response
from fastapi.responses import JSONResponse

router = APIRouter()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


items_db = [
    Item(name="Soup", description="Clear Soup", price=4.99, tax=2.99),
    Item(name="Dumpling", description="Chicken Dumpling", price=8.99, tax=2.99),
    Item(
        name="Fried Rice",
        description="Thai Fried Rice with Tofu",
        price=12.99,
        tax=2.99,
    ),
]


@router.get("/")
async def get_items() -> list[Item]:
    return items_db


@router.post("/", status_code=201)
async def create_item(item: Item) -> Item:
    items_db.routerend(item)
    return item


@router.get(
    "/{item_id}",
    response_model=Item,
    response_model_include=["name", "description"],
)
async def get_item(item_id: int):
    return items_db[item_id - 1]


@router.get("/{item_id}/public", response_model=Item, response_model_exclude=["tax"])
async def get_item_public(item_id: int):
    return items_db[item_id - 1]


@router.put("/{item_id}")
async def update_item(item_id: int, item: Item) -> Item:
    items_db[item_id - 1] = item
    return items_db


@router.delete("/{item_id}")
async def delete_item(item_id: int) -> Response:
    del items_db[item_id - 1]
    return JSONResponse(content={"message": "Item deleted successfully"})
