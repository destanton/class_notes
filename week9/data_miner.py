import requests

# response = requests.get("http://projects.fivethirtyeight.com/2016-election-forecast/updates.json")
# # print(response.text) if just doing web scraping w/ BeautifulSoup
# # pp.pprint(response.json())  # if using json w/ api
# response_json = response.json()
# # pp.pprint(response_json.keys())
# latest = response_json["updates"][0]
# # latest_id = response_json["updates"][0]["added"]
# latest_id = latest["added"]
# # print(latest_id)
# # pp.pprint(latest.keys())
# diffs = latest["diffs"]
# # pp.pprint(diffs["now-cast"])
# base_sms = ""
# for candidate in diffs["now-cast"]:
#     current = float(candidate["winprob"]["current"])
#     previous = float(candidate["winprob"]["prev"])
#     diff = round((current - previous) * 100, 2)
#     base_sms += "{}: {}. Diff: {}\n".format(candidate["candidate"], current * 100, diff)
#     # print(float(candidate["winprob"]["current"]) * 100)
#     # print(current * 100)
#     # print(diff)
# print(base_sms)


class DataMiner:

    def __init__(self):
        self.url = "http://projects.fivethirtyeight.com/2016-election-forecast/updates.json"
        self.response_json = []
        self.latest = {}
        self.latest_id = 0
        self.last_id = 0
        self.diffs = []
        self.base_sms = ""

    def get_data(self):
        self.response_json = requests.get(self.url).json()
        self.latest = self.response_json["updates"][0]
        self.latest_id = self.latest["added"]
        self.diffs = self.latest["diffs"]

    @property
    def is_new_data(self):
        self.get_data()
        if self.latest_id == self.last_id:
            return False
        self.last_id = self.latest_id
        return True

    @property
    def message(self):
        base_sms = ""
        for candidate in self.diffs["now-cast"]:
            current = float(candidate["winprob"]["current"])
            previous = float(candidate["winprob"]["prev"])
            diff = round((current - previous) * 100, 2)
            base_sms += "{}: {}. Diff: {}\n".format(candidate["candidate"], current * 100, diff)
            # print(float(candidate["winprob"]["current"]) * 100)
            # print(current * 100)
            # print(diff)
        self.base_sms = base_sms
        return self.base_sms
        # print(base_sms)
