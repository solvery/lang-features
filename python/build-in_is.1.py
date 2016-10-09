
# is
b = a = 1
print a is b
print a is not b
print id(a) == id(b)

print  
b = 2
print a is b

# int vs float
# 和core Python书中结果不一致
print  
a = 1
b = 1
print id(a) 
print id(b)

print  
a = 2.0
b = 2.0
print id(a) 
print id(b)
