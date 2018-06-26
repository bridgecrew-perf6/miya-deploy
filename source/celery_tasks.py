import os
import time

from celery_app import app
from config import CELERY_BROKER_URL, CELERY_RESULT_BACKEND


@app.task
def long_task():   
    time.sleep(10)
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print("Long Task:    " + now)
    return "Long Task Done"


@app.task
def hello(message):
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print(message + "    " + now)
    return "Done!"
    