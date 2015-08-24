
# lambda [arg1[, arg2, ... argN]]: expression

lambda :True

a = lambda x, y=2: x + y
print a(3)
print a(3, 5)

print 
b = lambda *z: z
print b(123, 'xyz')
print b(22)
