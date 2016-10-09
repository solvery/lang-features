# set
print
s = set('cheeseshop')
print s
t = frozenset('bookshop')
print t
print type(s)
print type(t)
print 'k' in s
s.add('z')
s.update('pypi')
s.remove('z')
s -= set('pypi')
print s | t
print s & t
print s - t
print s ^ t
s |= set('pypi')
s &= set('shop')
s -= set('shop')

for i in s:
    print i

