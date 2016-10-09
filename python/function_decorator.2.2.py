#encoding=utf-8

from inspect import getmembers, getargspec
from functools import wraps
import inspect

def wraps_decorator(f):
    @wraps(f)
    def wraps_wrapper(*args, **kwargs):
        return f(*args, **kwargs)
    return wraps_wrapper

def get_true_argspec(method):
    argspec = inspect.getargspec(method)
    args = argspec[0]
    if args and args[0] == 'self':
        return argspec
    if hasattr(method, '__func__'):
        method = method.__func__
    if not hasattr(method, 'func_closure') or method.func_closure is None:
        raise Exception("No closure for method.")

    method = method.func_closure[0].cell_contents
    return get_true_argspec(method)


class SomeClass(object):
    @wraps_decorator
    def method(self, x, y):
        pass

obj = SomeClass()
for name, func in getmembers(obj, predicate=inspect.ismethod):
    print "Member Name: %s" % name
    print "Func Name: %s" % func.func_name
    print "Args: %s" % getargspec(func)[0]
    print "Args: %s" % get_true_argspec(func)[0]

# 输出：
# Member Name: method
# Func Name: method
# Args: [] 

