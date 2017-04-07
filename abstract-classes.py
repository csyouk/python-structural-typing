from abc import ABC
from collections.abc import Iterable


class MyTuple(ABC):
    pass

MyTuple.register(tuple)


class MyIterable:
    def __iter__(self):
        return []


if __name__ == '__main__':

    assert issubclass(tuple, MyTuple)
    assert isinstance((), MyTuple)
    assert isinstance(MyIterable(), Iterable)
