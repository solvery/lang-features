
def foo(d1, d2):
    print "foo 1 invoked"

def foo(data):
    print "foo 2 invoked"

#foo(1,2) error
foo(1234)
