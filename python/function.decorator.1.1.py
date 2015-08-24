#encoding=utf-8

#给函数调用做缓存
# 在调用函数前查询一下缓存，如果没有才调用了，有了就从缓存中返回值。
# 从二叉树式的递归成了线性的递归。

from functools import wraps

def memo(fn):
    cache = {}
    miss = object()

    @wraps(fn)
    def wrapper(*args):
        result = cache.get(args, miss)
        if result is miss:
            result = fn(*args)
            cache[args] = result
        return result

    return wrapper

@memo
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

print fib(8)
