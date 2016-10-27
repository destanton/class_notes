import requests  # library that allows us to talk to the internet
import time

url = "http://swapi.co/api/people/1/"

json_result = requests.get(url).json()

films = json_result.get("films", "")

# for film in films:
#     print(film)

for film in films:
    film_result = requests.get(film).json()
    # print(film_result["opening_crawl"].split("\r\n"))
    split_crawl = (film_result["opening_crawl"].split("\r\n"))
    for line in split_crawl:
        print(line)
        time.sleep(1)  # slows the program down
