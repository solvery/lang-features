
# string
s = 'abcdefgh'
print s
print s[::-1] 
print s[::2]
for i in [None] + range(-1, -len(s), -1):
    print s[:i]

print
foo = "abc"
for i in range(len(foo)):
    print foo[i], '(%d)' % i

# list
print
aList = [1, 2, 3, 4]
print aList
print aList*3
print aList[0]
print aList[2:]
print aList[:3]
print ['a', 'b'] + ['c', 'd']!
print list("abcd")!
print [x for x in range(3)]

aList[1] = 5
print aList

# tuple
print
aTuple = ('robots', 77, 93, 'try')
print aTuple
print aTuple[0]
print aTuple[2:]

# dict
print
aDict = {'host': 'earth'}
print aDict

aDict['port'] = 80
aDict['arch'] = 'arm'
print aDict

aDict.keys()
aDict.values()
aDict.items()
aDict.get('host')
aDict['host']
print 'host' in aDict

# for key in aDict.keys(): , old method
# iterator
for key in aDict:
    print key, aDict[key]

edict = {}.fromkeys(('foo', 'bar'))

# dict other method 
dict(zip(('x', 'y'), (1, 2)))
dict([['x', 1], ['y', 2]])
dict([('xy'[i-1], i) for i in range(1,3)])
dict(x=1, y=2)
dict8 = dict(x=1, y=2)
dict9 = dict(**dict8)
dict9 = dict8.copy()

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
