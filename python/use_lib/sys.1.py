
# ref counter
import sys

x=1234

print sys.getrefcount(x)
a=x
print sys.getrefcount(x)
del a
print sys.getrefcount(x)

print
print globals()
print globals() is locals()

