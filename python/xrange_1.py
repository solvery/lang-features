#encoding=utf-8
# xrange生成的不是一个数组，而是一个生成器。
# 3.x里面，range就是xrange了

print (xrange(5))
print list(xrange(5))
