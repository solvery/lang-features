
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


