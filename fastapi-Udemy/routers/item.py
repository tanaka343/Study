from typing import Annotated
from fastapi import APIRouter,Body,Depends
from cruds import item as item_cruds
from schemas import ItemCreate
from database import get_db
from sqlalchemy.orm import Session

DbDependency = Annotated[Session,Depends(get_db)]

#prefix共通設定
router = APIRouter(prefix="/items",tags=["Items"])

@router.get("")
async def find_all(db: DbDependency):
    return item_cruds.find_all(db)

@router.get("/{id}")
async def find_by_id(db: DbDependency,id: int):
    return item_cruds.find_by_id(db,id)

@router.get("/")
async def find_by_name(db :DbDependency,name: str):
    return item_cruds.find_by_name(db,name)
 
@router.post("")
async def create(db: DbDependency,item_create: ItemCreate):
    return item_cruds.create(db,item_create)

@router.put("/{id}")
async def update(db :DbDependency,id :int,item_update = Body()):
    return item_cruds.updata(db,id,item_update)

@router.delete("/{id}")
async def delete(db: DbDependency,id :int):
    return item_cruds.delete(db,id)