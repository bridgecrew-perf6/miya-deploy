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
        print('TestHandler done')
        r.get()
        self.write({'task': r.result})


class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        print('hello')
        self.write('hello')


class LongTaskHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        r = long_task.delay()
        print('LongTaskHandler done')
        r.get()
        self.write(json.dumps(r.result))


def f2s():
    print('2s ', datetime.datetime.now())


def f5s():
    print('5s ', datetime.datetime.now())
