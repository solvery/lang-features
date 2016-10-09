
def foo(x):
    def a():
        print x

    print hex(id(a))
    return a

a1 = foo(100)
a2 = foo('hi')

print a1
print a2
a1()
a2()
print a1.func_closure
print a2.func_closure
print a1.func_code is a2.func_code

print foo.func_code.co_cellvars
print a1.func_code.co_cellvars
