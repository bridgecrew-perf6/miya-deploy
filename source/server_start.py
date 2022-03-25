# coding=utf-8
import tornado
import tornado.httpserver
import tornado.httpserver
import tornado.ioloop
import tornado.web
from tornado.log import enable_pretty_logging

import app_handle
from config import WEB_PORT


# -*- coding: utf-8 -*-


class MyApp:
    def __init__(self, port=WEB_PORT):
        self._port = port

        self._handlers = [
            (r'/hello', app_handle.HelloHandler),
            (r'/long', app_handle.LongTaskHandler),
            (r'/test', app_handle.TestHandler)
        ]

        self._settings = dict(
            debug=True
        )

        self._tornado_app = tornado.web.Application(
            handlers=self._handlers,
            settings=self._settings)
        enable_pretty_logging()
        self._http_server = tornado.httpserver.HTTPServer(self._tornado_app)
        tornado.ioloop.PeriodicCallback(app_handle.f2s, 2000).start()  # start scheduler 每隔2s执行一次f2s
        tornado.ioloop.PeriodicCallback(app_handle.f5s, 5000).start()  # start scheduler
        self._io_loop = tornado.ioloop.IOLoop.current()

    def start(self):
        self._http_server.listen(self._port)
        self._io_loop.start()


def server_start():
    app = MyApp()
    app.start()


if __name__ == "__main__":
    server_start()
