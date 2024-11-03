from fastapi import FastAPI, Path, Body, Cookie, Header
from pydantic import BaseModel
from datetime import datetime
from fastapi import Depends
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer


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
    tags: list[int] = []



# @app.get("/items")
# async def get_items(
#     cookie_id: str |None = Cookie(None),
#     accept_encoding: str | None = Header(None),
#     sec_ch_ua: str | None = Header(None),
#     user_agent: str | None = Header(None),
#     x_token: list[str] | None = Header(None)
# ):
#     items = {
#         "cookie_id": cookie_id,
#         "accept_encoding": accept_encoding,
#         "sec_ch_ua": sec_ch_ua,
#         "user_agent": user_agent,
#         'X-Tokens': x_token
#     }
#     return items

async def query_extractor(q: str|None = None):
    return q

async def query_or_body_extractor(
    q: str = Depends(query_extractor),
    last_q: str| None = Body(None)
):
    if not q:
        return last_q
    return q

oauthpasswordbearer = OAuth2PasswordBearer(tokenUrl="token")

@app.post("/item")
async def try_query(query_or_body: str = Depends(query_or_body_extractor), token: str = Depends(oauthpasswordbearer)):
    return {"q_or_body": query_or_body}