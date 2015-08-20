
# list
aList = [1, 2, 3, 4]
print aList
print aList[0]
print aList[2:]
print aList[:3]

aList[1] = 5
print aList

# tuple
aTuple = ('robots', 77, 93, 'try')
print aTuple
print aTuple[0]
print aTuple[2:]

# dict
aDict = {'host': 'earth'}
print aDict

aDict['port'] = 80
print aDict

aDict.keys()
aDict['host']

for key in aDict:
    print key, aDict[key]
