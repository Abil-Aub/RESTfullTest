import requests

res = requests.post("http://127.0.0.1:3000/api/courses/3", {"name": "C++", "videos": 12})
print(res.json())
