from kvhell.kv_base import KvBase


class KvMemory(KvBase):

    def __init__(self):
        self.__store = dict()

    def get(self, key):
        return self.__store[key]

    def put(self, key, value):
        self.__store[key] = value

    def delete(self, key):
        del self.__store[key]

    def reset(self):
        self.__store = dict()