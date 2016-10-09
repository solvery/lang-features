
def foo():
    for i in range(3):
        def a():
            print i
        yield a

a, b, c = foo()

a()
b()
c()

