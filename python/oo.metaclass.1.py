
from abc import ABCMeta
class MyABC:
    __metaclass__ = ABCMeta

MyABC.register(tuple)
print issubclass(tuple, MyABC)
print isinstance((), MyABC)
