
# override __init__
class P(object):
    def __init__(self):
        print 'call in P'

class C1(P):
    def __init__(self):
        print 'call in C1'

class C2(P):
    def __init__(self):
        P.__init__(self)
        print 'call in C2'

class C3(P):
    def __init__(self):
        super(C3, self).__init__()
        print 'call in C3'

c1 = C1()

print
c2 = C2()

print
c3 = C3()
