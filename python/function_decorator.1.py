
# classmethod()和staticmethod()内置函数


class C:
    def foo(cls, y):
        print "classmethod", cls, y
    foo = classmethod(foo)

class C:
    @classmethod
    def foo(cls, y):
        print "classmethod", cls, y
