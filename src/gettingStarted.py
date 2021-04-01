from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI() # load up fx

class Item(BaseModel): # python class
    name: str
    price: float
    is_offer: Optional[bool] = None

@app.get("/") # annotations like spring boot
def read_root(): # controller for get / 
    return {"Hello": "World"} # dict 


@app.get("/items/{item_id}") # example of accepting param
def read_item(item_id: int, q: Optional[str] = None): # example of receiving query string
    return {"item_id": item_id, "q": q}