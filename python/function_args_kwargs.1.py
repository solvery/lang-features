#encoding=utf-8

# *args表示任何多个无名参数，它是一个tuple
# **kwargs表示关键字参数，它是一个dict
# 同时使用*args和**kwargs时，*args参数列必须要在**kwargs前

def test_param(*args):
    print args

def test_param_2(**args):
    print args

test_param('test1', 'test2')
test_param_2(p1='test1', p2='test2')

# 
print 
def foo(*args,**kwargs):
    print 'args=',args
    print 'kwargs=',kwargs
    print 

foo(1,2,3)
foo(a=1,b=2,c=3)
foo(1,2,3,a=1,b=2,c=3)
foo(1,'b','c',a=1,b='b',c='c')
