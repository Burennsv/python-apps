from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel): 
    name: str 
    description: str

Items_array = {
    1:{
        "name": "First",
        "description": "First element. Defined via code"
    },
    2:{
        "name": "Second",
        "description": "This element goes after first element"
    }
    }

app = FastAPI()


@app.get("/array")
async def read_items():
    return Items_array

@app.get("/search_by_name/{item_name}")
async def get_item(item_name: str):   
    for item_id in Items_array:
        if Items_array[item_id]["name"] == item_name:
            return Items_array[item_id]
    return {"Error": "There are no item with this name"}

@app.get("/search_by_id/{item_id}")
async def get_item(item_id: int):
    if item_id in Items_array:
        return Items_array[item_id]
    return {"Error": "There are no item with this id"}

@app.post("/create_item/{item_id}")
async def create_item(item_id, item: Item):
    if item_id in Items_array:
        return{"Error": "Item already exists"}
    Items_array[item_id] = item
    return Items_array[item_id]