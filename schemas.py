
from pydantic import BaseModel

class CustomerBase(BaseModel):
    name: str
    email: str

class CustomerCreate(CustomerBase):
    password: str

class CustomerResponse(CustomerBase):
    id: int

    class Config:
        orm_mode = True

class ProductBase(BaseModel):
    name: str
    price: float

class ProductResponse(ProductBase):
    id: int
    
    class Config:
        orm_mode = True

class OrderBase(BaseModel):
    customer_id: int
    product_id: int
    quantity: int

class OrderResponse(OrderBase):
    id: int

    class Config:
        orm_mode = True