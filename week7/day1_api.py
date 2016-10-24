import requests

# url = "http://swapi.co/api/people"
# while url:
#     result = requests.get(url)
#     json_result = result.json()
#
#     # print(json_result['results'])
#
#     for person in json_result["results"]:
#         print(person["name"])
#
#     url = json_result["next"]
# result = requests.get(url)
# # result = requests.get(json_result["next"])
# json_result = result.json()
#
# for person in json_result['results']:
#     print(person['name'])


def get_data(endpoint, lookup="name"):
    url = "http://swapi.co/api/{}/".format(endpoint)
    while url:
        result = requests.get(url)
        json_result = result.json()

        # print(json_result['results'])

        for person in json_result["results"]:
            print(person[lookup])
        if input("Press Enter to keep going. Type 'n' to stop "):
            break
        url = json_result["next"]

# get_data("people")
# get_data("films", lookup="title")

while True:
    value = input("what do you want to search for? (films) or (people): ")
    get_data(value)
