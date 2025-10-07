from fastapi import FastAPI,Body
from cruds import items as item_cruds

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items")
async def find_all():
    return item_cruds.find_all()

@app.get("/items/{id}")
async def find_by_id(id: int):
    return item_cruds.find_by_id(id)

@app.post("/items")
async def create_item(create_item = Body()):
    return item_cruds.create(create_item)

@app.put("/items/{id}")
async def update_date(id :int,update_item = Body()):
    return item_cruds.update_data(id,update_item)

@app.delete("/items/{id}")
async def delete_data(id :int):
    return item_cruds.delete_data(id)