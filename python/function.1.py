
# Inner or Nested Functions
def f1():
    def f2():
        pass

# Forward References
def f3():
    f4()

def f4():
    pass


# multi reutrn value
def foo():
    return ['zxy', 1000, -99]

def bar():
    return 'abc', [42, 'python'], "Guido"

aTuple = bar()
x, y, z = bar()
(x, y, z) = bar()

# argument
def net_conn(host, port):
    pass

net_conn('kappa', 8080)
# keyword argument
net_conn(port=8080, host='chino')

# default argument
def net_conn2(host, port=80):
    pass

net_conn2('kappa')

