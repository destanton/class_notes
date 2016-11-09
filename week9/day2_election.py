# import pprint
import time
# pp = pprint.PrettyPrinter(indent=2)
# import requests  # a headless web browser. get the data.
# from bs4 import BeautifulSoup
from data_miner import DataMiner
from messenger import Messenger


messenger = Messenger()
dm = DataMiner()
while True:
    print("is there new data?")
    if dm.is_new_data:
        base_sms = dm.message
        print("New Data!")
        messenger.send(base_sms)
    # print(dm.is_new_data)
    time.sleep(1800)
# dm.get_data()
