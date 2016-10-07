#encoding=utf-8

with open('abc.txt', 'r') as f:
   print

# 等价于
try:
    f = open('abc.txt', 'r')
except:
    pass
else:
    print
finally:
    f.close()
