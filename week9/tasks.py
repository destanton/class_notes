# all work that needs to happen async
import time
import random
import datetime
from celery import Celery
import requests


app = Celery('tasks')


@app.task
def cal_decombobulator_xy():
    now = datetime.datetime.now()
    time.sleep(random.randint(0, 5))
    print(now)


@app.task
def kill_joel():
    requests.get("http://10.0.10.221:8000")
