
x = "aa"
print id(x)
x = "bb"
print id(x)

print
i = 0
print id(i)
i = i+1
print id(i)

print 
aList = ['ammonia', 83, 85, 'lady']
print id(aList)
aList[2] = aList[2] + 1
print id(aList)
aList.append('gaudy')
aList.append(aList[2] + 1)
print id(aList)


