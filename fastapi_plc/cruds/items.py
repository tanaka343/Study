from typing import Optional
from enum import Enum

class ItemStatus(Enum):#（エナム）は「列挙型」と呼ばれるもので、決まった選択肢（値）のみを持つ特別な型です。
    ON = "ON"
    SOLD = "SOLD"

class Item:
    # class Sample:
    # def __init__(self, 引数1, 引数2):
    #     self.属性1 = 引数1
    #     self.属性2 = 引数2

    def __init__(#引数に型ヒントをつけたもの
            self,
            id :int,
            name :str,
            description :Optional[str],#None or string
            status: ItemStatus
    ):
        self.id = id
        self.name = name
        self.description = description
        self.status = status


items = [
    
    Item(1,"ばなな",None,ItemStatus.ON),
    Item(2,"アボカド",None,ItemStatus.ON),
    Item(3,"紅茶",None,ItemStatus.ON),
    Item(4,"ばなな",None,ItemStatus.ON),
]

def find_all():
    return items

def find_by_id(id : int):
    for item in items:
        if item.id == id:
            return item
    return None#位置に注意

def create(create_item):
    c_item = Item(
        len(items)+1,
        create_item.get("name"),
        create_item.get("description"),
        ItemStatus.ON,
    )
    items.append(c_item)
    return items

def update_data(id: int,update_item):
    for item in items:
        if item.id == id:
            item.name = update_item.get("name",item.name)
            item.description = update_item.get("description",item.description)
            item.status = update_item.get("status",item.status)
            return item
    return None

def delete_data(id: int):
    for i in range (len(items)):
        if items[i].id==id:
            delete_item = items.pop(i)
            return delete_item
    return None
