# when function end, generator throw StopIteration exception. 

def fab(max):
    n, a, b = 0, 0, 1
    while n<max:
        yield b 
        # print b
        a, b = b, a+b
        n = n+1

for n in fab(5):
    print n

# 
print 
from inspect import isgeneratorfunction
print isgeneratorfunction(fab)

# 
print
import types
print isinstance(fab,     types.GeneratorType)
print isinstance(fab(5),  types.GeneratorType)
from collections import Iterable
print isinstance(fab,     Iterable)
print isinstance(fab(5),  Iterable)

