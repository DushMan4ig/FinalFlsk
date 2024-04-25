from pydantic import BaseModel
from typing import List, Optional

# Модель для таблицы "Пользователи"
class UserBase(BaseModel):
    first_name: str
    last_name: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

# Модель для таблицы "Товары"
class ItemBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True

# Модель для таблицы "Заказы"
class OrderBase(BaseModel):
    user_id: int
    item_id: int
    order_date: Optional[str] = None
    status: Optional[str] = None

class Order(OrderBase):
    id: int

    class Config:
        orm_mode = True
