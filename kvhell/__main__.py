#!/usr/bin/python
# coding=utf-8

import tornado.ioloop
import tornado.web
from kvhell.kv_memory import KvMemory


class KvHandler(tornado.web.RequestHandler):

    def initialize(self, kv_store):
        self.__kv_store = kv_store

    def get(self, key):
        value = self.__kv_store.get(key)
        self.write(value)

    def put(self, key):
        self.__kv_store.put(key, self.request.body)

    def delete(self, key):
        if key == "":
            self.__kv_store.reset()
        else:
            self.__kv_store.delete(key)

    def head(self, key):
        """
        HEAD http verb is used as a health check on the application.
        If tornado server is stop, this url doesn't returns answer
        """
        pass

def make_app():
    kv_store = KvMemory()
    return tornado.web.Application([
        (r"/(.*)", KvHandler, dict(kv_store=kv_store)),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
