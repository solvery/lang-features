
import copy

# deep and shallow copy, is talk about status sub-object in a object.

a = [1,2,3,4,['a', 'b']]
a1 = a
a2 = a[:]
a3 = copy.copy(a)
a4 = copy.deepcopy(a)

a.append(5)
a[4].append('c')

print '\t', a
print '=\t', a1
print '[:]\t', a2
print 'copy\t', a3
print 'deep\t', a4

