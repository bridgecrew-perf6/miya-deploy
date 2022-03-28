import time

from celery_app import app


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


@app.task
def mytask0(task_name):
    print("task0:%s" % task_name)
    return task_name


@app.task
def mytask1(task_name):
    print("task1:%s" % task_name)
    return task_name
