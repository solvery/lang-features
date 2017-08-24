
import random

list_char = []
for i in range(48,58):
    list_char += chr(i)
for i in range(65,91):
    list_char += chr(i)
for i in range(97,123):
    list_char += chr(i)

print list_char

with open ('data.txt', 'w') as fd:
    for i in range(200000):
        l = random.shuffle(list_char)
        s = ''.join(list_char)
        s += '\n'
        fd.write(s)
