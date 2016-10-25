import requests

json_results = requests.get("http://localhost:8000/specials/").json()
# print(json_results)
# count = 0
# while True:
    # json_results = requests.get("http://localhost:8000/specials/").json()
    # print(count)
    # count += 1
for special in json_results:
    print(special["name"])
    print(special["price"])
    print("*" * 50)
