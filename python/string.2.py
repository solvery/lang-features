
# string
str1 = 'abcdefgh'
print str1
print str1[::-1]    # 逆序
print str1[::2]     # 步进=2

for i in [None] + range(-1, -len(str1), -1):
    print str1[:i]


