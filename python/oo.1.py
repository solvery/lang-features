

class A:
    def m1(self):
        print 'm1'
    def m2(self, ):
        pass

A.x = 1;
A.y = 1;

oa = A()
print oa.x
oa.z = 1;
print oa.z

oa.m1()

class B(A):
    pass

ob = B()
print ob.x
ob.m1()
