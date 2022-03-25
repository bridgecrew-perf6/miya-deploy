# coding=utf-8
import datetime
import json

import tornado
from tornado import gen
from tornado import web

from celery_tasks import long_task, mytask0


class TestHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        r = mytask0.apply_async(
            args=['task0'],
            queue='mytask0',
            routing_key='celery_tasks.mytask0')
        while True:
            if r.ready() is True:
                break
            yield gen.sleep(1)
        print('TestHandler done')
        self.write({'task': r.result})


class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        print('hello')
        self.write('hello')


class LongTaskHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        data = long_task.delay()

        while True:
            if data.ready() is True:
                break
            yield gen.sleep(1)
        print('LongTaskHandler done')
        self.write(json.dumps(data.result))


def f2s():
    print('2s ', datetime.datetime.now())


def f5s():
    print('5s ', datetime.datetime.now())
