from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3




app = FastAPI()

# Database setup
conn = sqlite3.connect('orders.db', check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS orders
                (id INTEGER PRIMARY KEY, symbol TEXT, price FLOAT, quantity INTEGER, order_type TEXT)''')
conn.commit()



# Pydantic model for request validation
class Order(BaseModel):
    symbol: str
    price: float
    quantity: int
    order_type: str

# POST /orders
@app.post("/orders")
async def create_order(order: Order):
    cursor.execute('''INSERT INTO orders (symbol, price, quantity, order_type)
                    VALUES (?, ?, ?, ?)''', (order.symbol, order.price, order.quantity, order.order_type))
    conn.commit()
    order_id = cursor.lastrowid 
    return {"message": "Order created successfully", "order_id": order_id}

# GET /orders
@app.get("/orders")
async def get_orders():
    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()
    return {"orders": orders}



