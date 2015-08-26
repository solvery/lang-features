
#  method resolution order.
# MRO Problems Caused by Diamonds

class A(object):
    pass

class B(A):
    pass

class C(A):
    def __init__(self):
        print 'C init.'

class D(B, C):
    pass

d = D()
print D.__mro__
print A.__subclasses__()


