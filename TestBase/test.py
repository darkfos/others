import requests as req


data = req.get("http://127.0.0.1:8000/book/all")
print(data.json())