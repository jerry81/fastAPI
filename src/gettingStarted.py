from typing import Optional, List

from uuid import UUID
from datetime import datetime, time, timedelta

from enum import Enum

from fastapi import FastAPI, Query, Body, Path
from pydantic import BaseModel, Field

app = FastAPI()  # load up fx

class Image(BaseModel):
    url: str
    name: str

class Item(BaseModel):
    name: str
    description: Optional[str] = Field( # field validator
       None, title="The description of the item", max_length=300
    )
    price: float = Field(..., gt=0, description="The price must be greater than zero")
    tax: Optional[float] = None
    tags: List[str] = []
    image: Optional[Image] = None # subModel as type

    class Config: # note that this is part of the Class, schema declaration, aids in docs
        schema_extra = {
            "example": {
                "name": "Foo",
                "description": "A very nice Item",
                "price": 35.4,
                "tax": 3.2,
            }
        }


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

class User(BaseModel):
    username: str
    full_name: Optional[str] = None

class UserIn(BaseModel):
    username: str
    password: str
    email: str
    full_name: Optional[str] = None

class UserOut(BaseModel):
    username: str
    email: str
    full_name: Optional[str] = None


@app.get("/")  # annotations like spring boot
def read_root():  # controller for get /
    return {"Hello": "World"}  # dict


@app.put("/items/{item_id}")
# both param and body and query param too
def update_item(*, item_id: int, item: Item, q: Optional[str] = None, user: User): # multiple bodies
    return {"item_id": item_id, **item.dict()}  # double star unpacks dict

@app.put("/itemsWithDate/{item_id}")
async def read_items(
    item_id: UUID,
    start_datetime: Optional[datetime] = Body(None),
    end_datetime: Optional[datetime] = Body(None),
    repeat_at: Optional[time] = Body(None),
    process_after: Optional[timedelta] = Body(None),
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration,
    }

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
        *,  # without this, you cannot put non-defaults after params with defaults
        item_id: int = Path(..., title="the ID", ge=1, le=1000), 
        q: str,
        size: float = Query(..., gt=0, lt=10.5)): # float example
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

@app.post("/userWithResponseModel/", response_model=UserOut, response_model_exclude_unset=True)
async def create_user(user: UserIn):
    return user