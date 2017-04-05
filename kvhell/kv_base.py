from abc import ABCMeta, abstractmethod

class KvBase(object):
    """
    contract of the key value store we want to implement.
    Every implementation has to inherit this contract to be
    compliant with the system we want to build
    """
    __metaclass__ = ABCMeta

    @abstractmethod
    def get(self, key):
        pass

    @abstractmethod
    def put(self, key, value):
        pass

    @abstractmethod
    def delete(self, key):
        pass

    @abstractmethod
    def reset(self):
        pass