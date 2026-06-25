import requests

response = requests.get("https://httpbin.org/get")
response.raise_for_status()
print(response.json())
