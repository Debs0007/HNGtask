import json
import requests

x = {
  "slackUsername": "Debs",
  "backend": True,
  "age": 22,
  "bio": "My name is Abdulhamid Lawal, i'm a beginner in backend development with little knowledge on python and i hope in gaining tremendous knowledge from HNG9 internship."
}
print(json.dumps(x))

d = requests.get('https://github.com/Debs0007/HNGtask.git', params=x)

