import requests
import time
from bs4 import BeautifulSoup

headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36"

}

################################## Search for a band
search_url = "http://search.azlyrics.com/search.php?q="
artist = "justin+timberlake"

body = requests.get(search_url + artist)  # body of html, simulates clicking a link
parser = BeautifulSoup(body.text, "html.parser")  # will find html.parser in printout in term.
# print(body.text)
# print(parser.find("a").get("href"))  # gets first href
# print(parser.findAll("a"))  # finds all a tags
# for counter, tag in enumerate(all_a_tags): # iterates through all tags and enumerates
#     print(counter, tag)
# print(next_page)
all_a_tags = parser.findAll("a")
next_page = all_a_tags[28].get("href")

# time.sleep(10)  # gives error on page, probably becuase of time request, so slow down request
######################### find all of their songs

body = requests.get(next_page, headers=headers)
parser = BeautifulSoup(body.text, "html.parser")
# all_a_tags = parser.findAll("a")
# print(all_a_tags)
all_a_tags = parser.findAll("a")[32:496]
song_link_list = []

for counter, tag in enumerate(all_a_tags):
    if not tag.get("rel") and tag.get("href"):
        song_link_list.append(tag.get("href"))
    # print(counter, tag.get("rel"))

for song_link in song_link_list:
    new_song_link = song_link.replace("..", "http://www.azlyrics.com")
    song_page = requests.get(new_song_link, headers=headers)
    parser = BeautifulSoup(song_page.text, "html.parser")
    all_divs = (parser.findAll("div"))
    song_div = parser.findAll("div")[22]
    # for counter, div in enumerate(all_divs):
    #     print(counter, div)
    print(song_div.text)
    input()
