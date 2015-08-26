
#  method resolution order.
# MRO Problems Caused by Diamonds

class B:
    pass

class C:
    def __init__(self):
        print 'C init.'

class D(B, C):
    pass

d = D()

