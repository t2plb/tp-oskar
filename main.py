from fastapi import FastAPI, Depends
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from typing import List

import models
from database import engine, get_db
from schemas import CustomerCreate, CustomerResponse, ProductResponse, OrderResponse
import controllers

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="TP API FastAPI",
    description="Hello guys welcome.",
    version="1.0.0"
)

@app.get("/customers/", response_model=List[CustomerResponse])
def get_customers(db: Session = Depends(get_db)):
    return controllers.get_customers(db)

@app.get("/products/", response_model=List[ProductResponse])
def get_products(db: Session = Depends(get_db)):
    return controllers.get_products(db)

@app.get("/orders/", response_model=List[OrderResponse])
def get_orders(db: Session = Depends(get_db)):
    return controllers.get_orders(db)

@app.get("/customers/{customer_id}", response_model=CustomerResponse)
def get_customer(customer_id: int, db: Session = Depends(get_db)):
    return controllers.get_customer(db, customer_id)

@app.get("/products/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):
    return controllers.get_product(db, product_id)

@app.get("/orders/{order_id}", response_model=OrderResponse)
def get_order(order_id: int, db: Session = Depends(get_db)):
    return controllers.get_order(db, order_id)

@app.post("/customers/", response_model=CustomerResponse)
def create_customer(customer: CustomerCreate, db: Session = Depends(get_db)):
    return controllers.create_customer(db, customer)

@app.delete("/customers/{customer_id}")
def delete_customer(customer_id: int, db: Session = Depends(get_db)):
    return controllers.delete_customer(db, customer_id)

client = TestClient(app)

def test_read_main():
    response = client.get("/customers/")
    assert response.status_code == 200

# on test si il y a une commande avec un article id 1

def test_read_order():
    response = client.get("/orders/1")
    assert response.status_code == 200