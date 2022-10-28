import requests

api_url = "https://github.com/Debs0007/HNGtask.git"
response = requests.get(api_url)
response.json()
