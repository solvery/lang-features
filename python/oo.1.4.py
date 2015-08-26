
# class build in method

class A(object):
    pass

class B(A):
    pass

class C(A):
    def __init__(self):
        print 'C init.'

class D(B, C):
    pass

a = A()
b = B()
c = C()
d = D()

print issubclass(B,A)
print issubclass(D,A)
print issubclass(D,B)
print issubclass(B,B)
print issubclass(A,B) # false

print
print isinstance(a,A)
print isinstance(b,A)
print isinstance(d,A)

print 
print vars(c)
