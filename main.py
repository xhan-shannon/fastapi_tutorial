from fastapi import FastAPI, Path
from pydantic import BaseModel


app = FastAPI()

# @app.get("/")
# async def root():
#     return {"message": "hello world!"}


# @app.post("/")
# async def post_handler():
#     return {"message": "hello from post"}

# @app.get("/items")
# async def get_all_items():
#     return {"message": "all itmes"}

# @app.get("/item/{item_id}")
# async def get_item(item_id: int):
#     return {"message": item_id}


# @app.get("/user/me")
# async def get_current_user():
#     return {"user": "current user xx"}


# @app.get("/user/{user_id}")
# async def get_user(user_id: str):
#     return {"user": user_id}


# class ProdItem(BaseModel):
#     name: str
#     description: str | None = None
#     price: float
#     tax: float | None = None


# @app.post("/items")
# async def post_item(item: ProdItem):
#     return item




#
# Part
#
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float


@app.put("/items/{item_id}")
async def update_item(
    item_id: int = Path(..., title="The ID of the item to get", ge=0, le=100),
    q: str | None = None,
    item: Item | None = None
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})

    return results