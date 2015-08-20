
# type
print type(1)
print type(type(1))
print type(type(type(1)))
print type(type)
print type("")
print type([])
print type({})
print type(())
print type(0+0j)

# cmp
print
a, b = -4, 12
print cmp(a, b)
b = -4 
print cmp(a, b)
a, b = 'abc', 'xyz'
print cmp(a, b)
print cmp(b, a)

# str repr ``
print 
print str(4.53-2j)
print str(2e10)

print 
print str([0, 5, 9, 9])
print repr([0, 5, 9, 9])
print `[0, 5, 9, 9]`

print
num = ""
print isinstance(num, (int, long, float, complex))

