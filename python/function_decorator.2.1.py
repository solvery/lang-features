#encoding=utf-8

# 消除Decorator的副作用
from functools import wraps
def hello(fn):
    @wraps(fn)
    def wrapper():
        print "hello, %s" % fn.__name__
        fn()
        print "goodby, %s" % fn.__name__
    return wrapper

@hello
def foo():
    '''foo help doc'''
    print "i am foo"
    pass

foo()
print foo.__name__ #输出 foo
print foo.__doc__  #输出 foo help doc


