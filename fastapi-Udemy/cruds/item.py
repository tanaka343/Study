from typing import Optional
from sqlalchemy.orm import Session
from enum import Enum
from schemas import ItemCreate
from models import Item

class ItemStatus(Enum):
    ON_SALE = "ON_SALE"
    SOLD_OUT = "SOLD_OUT"

# class Item:
#     def __init__(
#             self,
#             id:int,
#             name:str,
#             price:int,
#             description: Optional[str],
#             status: ItemStatus
#     ):
#         self.id = id
#         self.name = name
#         self.price = price
#         self.description = description
#         self.status = status

# items = [

#     Item(1,"PC",100000,"美品です",ItemStatus.ON_SALE),
#     Item(2,"スマートフォン",50000,None,ItemStatus.ON_SALE),
#     Item(3,"Python本",1000,"使用感あり",ItemStatus.SOLD_OUT),
# ]

def find_all(db :Session):
    return db.query(Item).all()


def find_by_id(db : Session,id: int):
    return db.query(Item).filter(Item.id == id).first()
    
def find_by_name(db : Session,name: str):
    return db.query(Item).filter(Item.name.like(f"%{name}%")).all()


def create(db: Session,item_create :ItemCreate):
    new_item = Item(
        **item_create.model_dump()
    )
    db.add(new_item)
    db.commit()
    return new_item

def updata(db: Session,id: int,item_update):
    item =find_by_id(db,id)
    if item is None:
        return None
    item.name = item_update.get("name",item.name)
    item.price = item_update.get("price",item.price)
    item.description = item_update.get("description",item.description)
    item.status = item_update.get("status",item.status)
    db.add(item)
    db.commit()
    return item
    

def delete(db: Session,id: int):
    item =find_by_id(db,id)
    if item is None:
        return None
    db.delete(item)
    db.commit()
    return item