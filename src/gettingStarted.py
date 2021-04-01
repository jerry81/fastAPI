from typing import Optional

from enum import Enum

from fastapi import FastAPI, Query
from pydantic import BaseModel

app = FastAPI()  # load up fx


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

class User(BaseModel):
    username: str
    full_name: Optional[str] = None


@app.get("/")  # annotations like spring boot
def read_root():  # controller for get /
    return {"Hello": "World"}  # dict


@app.put("/items/{item_id}")
# both param and body and query param too
def update_item(item_id: int, item: Item, q: Optional[str] = None, user: User): # multiple bodies
    return {"item_id": item_id, **item.dict()}  # double star unpacks dict


@app.get("/items/{item_id}")  # example of accepting param
# example of receiving query string
# short is another query param, remove the default to make it required
def read_item(item_id: int, q: Optional[str] = None, short: bool = False):
    return {"item_id": item_id, "q": q}


@app.get("/items/")
# validation example - max_length # first param is default value
async def read_items(q: Optional[str] = Query(None, min_length=3, max_length=50, regex="^fixedquery$")):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})  # for updating dicts
    return results


@app.get("/itemsTricks/")
# param validation (greater than or equal to 1)
async def read_items(
        *, 
        item_id: int = Path(..., title="the ID", ge=1, le=1000), 
        q: str,
        size: float = Query(... gt=0, lt=10.5)): # float example
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def getUser(user_id):
    return {"user_id": user_id}


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):  # use enum
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}


@app.post("/items/")
async def create_item(item: Item):  # request body
    item_dict = item.dict()
    if item.tax:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
        return item_dict
