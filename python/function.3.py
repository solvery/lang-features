
def foo(d1, d2):
    print "foo 1 invoked"

def foo(data):
    print "foo 2 invoked"

#foo(1,2) error
foo(1234)


def bar(d1, d2=0):
    print "bar invoked"

bar(1234)
bar(1234, 12)
