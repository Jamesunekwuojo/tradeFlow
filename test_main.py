from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_order():
    response = client.post("/orders", json={"symbol": "AAPL", "price": 150.0, "quantity": 10, "order_type": "buy"})
    assert response.status_code == 200
    assert "order_id" in response.json() 
    assert response.json() == {"message": "Order created successfully"}



def test_get_orders():
    response = client.get("/orders")
    assert response.status_code == 200
