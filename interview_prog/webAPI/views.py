from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    if request.method == 'POST':
        # Create product logic here
        pass
    token = requests.post("http://127.0.0.1:8000/api/v1/api-token-auth/", json={
		"username":"root",
		"password": "12345"
	})
    
    token = token.json().get("token", "")

    resp = requests.get(
        "http://127.0.0.1:8000/api/v1/products/",
        headers={
            "Authorization": f"Token {token}"
        }
    )
    return render(request, 'index.html', context={"data": resp.json()})