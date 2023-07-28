from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.get("/orders/me")
async def read_user_me():
    return {"user_id": "the current user"}


# This needs to be after /orders/me route
@app.get("/orders/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}
