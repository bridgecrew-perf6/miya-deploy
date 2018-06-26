# -*- coding: utf-8 -*-

import json
import sys
import signal
import time

import tornado.web
import tornado.httpserver
import tornado.ioloop
from tornado import gen

from celery_tasks import long_task
from config import WEB_PORT


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


class MyApp:
    def __init__(self, port=WEB_PORT):
        self._port = port

        self._handlers = [
            (r'/', HelloHandler),
            (r'/long', LongTaskHandler)
        ]

        self._settings = dict(
            debug=True
        )

        self._tornado_app = tornado.web.Application(self._handlers, **self._settings)
        self._http_server = tornado.httpserver.HTTPServer(self._tornado_app)
        self._io_loop = tornado.ioloop.IOLoop.current()

    def start(self):
        self._http_server.listen(self._port)
        self._io_loop.start()


if __name__ == '__main__':
    app = MyApp()
    app.start()
