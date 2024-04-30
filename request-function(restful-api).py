import requests

BASE = "http://127.0.0.1:5000/"

# data = [
#     {"likes": 80, "name": "Python Beginner Tutorial", "views": 10000},
#     {"likes": 1200, "name": "REST API Tutorial(Python)", "views": 100000},
#     {"likes": 1000, "name": "Machine Learning Tutorial(Beginner)", "views": 1000000},
# ]

# for i in range(len(data)):
#     response = requests.put(BASE + "video/" + str(i), json=data[i])
#     print(response.json())

# input()

response = requests.patch(BASE + "video/2", json={"views": 1500, "likes": 1200000})
print(response.json())
