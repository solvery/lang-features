#encoding=utf-8
# class式的 Decorator
# 1）一个是__init__()，给某个函数decorator时被调用，fn参数，被decorator的函数。
# 2）一个是__call__()，调用被decorator函数时被调用的。

class myDecorator(object):

    def __init__(self, fn):
        print "inside myDecorator.__init__()"
        self.fn = fn

    def __call__(self):
        self.fn()
        print "inside myDecorator.__call__()"

@myDecorator
def aFunction():
    print "inside aFunction()"

print "Finished decorating aFunction()"

aFunction()

