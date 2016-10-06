
# map filter replaced by list comprehension.
# reduce(func, [1, 2, 3]) = func(func(1, 2), 3)

d1 = range(9)
r1 = map(lambda x: x * x, d1)
r2 = filter(lambda x: x%3==0, d1)
r3 = reduce(lambda x,y:x+y, d1)
print d1
print r1
print [ x*x for x in d1]
print r2
print [ x for x in d1 if x%3==0]
print r3

