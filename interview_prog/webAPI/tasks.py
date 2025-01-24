from celery import shared_task
import requests
from uuid import uuid4

@shared_task
def create_prods():
    
    token = requests.post("http://127.0.0.1:8000/api/v1/api-token-auth/", json={
		"username":"root",
		"password": "12345"
	})
    
    token = token.json().get("token", "")

    resp = requests.post(
        "http://127.0.0.1:8000/api/v1/products/",
        headers={
            "Authorization": f"Token {token}",
            "Content-Type": "application/json"
        },
        json={
            "category_id": 1,
            "title": f"product_no_{uuid4()}",
            "description": "test desc",
            "price": 50.50,
            "status": 1
        }
    )
    print(resp.json())
    