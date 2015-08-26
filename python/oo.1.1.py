#encoding=utf-8

class C(object):
    foo = 100

    def methodA(self):
        pass

print C.foo
C.foo = C.foo + 1
print C.foo

objC = C();
objC.methodA()
# 没有实例，方法是不能被调用的, binding
# C.methodA()

print dir(C)
print dir(objC)
print C.__dict__
print objC.__dict__

# __bases__用来处理继承，它包含了一个由所有父类组成的元组。

# 实例属性 vs 类属性
print
c1 = C();
c2 = C();
print c1.foo
c1.foo = 1;
c2.foo = 2;
print c1.foo
print c2.foo
print C.foo

