from typing import Iterable, Iterator


class SupportClose(Iterable):

    def close(self) -> None:
        raise Exception("Close method not implemented")

    def not_doing_anything(self) -> None:
        raise Exception("any method not implemented")


class Resource:
    def close(self) -> None:
        print("close method implemented")

class Foo:
    pass

def close_all(things: Iterable[SupportClose]) -> None:
    for t in things:
        t.close()


if __name__ == '__main__':
    resource = Resource()
    resource.close()

    f = open('foo.txt')
    r = Resource()

    close_all([f, r])
    # close_all([1])

    print(type(SupportClose))
    print(type(Resource))
    print(type(Foo))