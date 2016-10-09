
#  method resolution order.

class P1:
    def foo(self):
        print 'foo in P1'

class P2:
    def foo(self):
        print 'foo in P2'

    def bar(self):
        print 'bar in P2'

class C1(P1, P2):
    pass

class C2(P1, P2):
    def bar(self):
        print 'bar in C2'

class A1(C1, C2):
    pass

a1 = A1()
a1.foo()
a1.bar()
C2.bar(a1)
P2.bar(a1)
# print A1.__mro__ only in new-style class

