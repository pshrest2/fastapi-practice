from typing import Any, List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import repos, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[schemas.Item])
async def get_items(
    owner_id: int, db: Session = Depends(deps.get_db), skip: int = 0, limit: int = 100
) -> Any:
    items = repos.item.get_multi_by_owner(
        db=db, owner_id=owner_id, skip=skip, limit=limit
    )

    return items


@router.post("/", status_code=201, response_model=schemas.Item)
async def create_item(
    *, db: Session = Depends(deps.get_db), item_in: schemas.ItemCreate
) -> Any:
    item = repos.item.create_with_owner(db=db, obj_in=item_in, owner_id=1)
    return item


# @router.get(
#     "/{item_id}",
#     response_model=Item,
#     response_model_include=["name", "description"],
# )
# async def get_item(item_id: int):
#     return items_db[item_id - 1]


# @router.put("/{item_id}")
# async def update_item(item_id: int, item: Item) -> Item:
#     items_db[item_id - 1] = item
#     return items_db


# @router.delete("/{item_id}")
# async def delete_item(item_id: int) -> Response:
#     del items_db[item_id - 1]
#     return JSONResponse(content={"message": "Item deleted successfully"})
