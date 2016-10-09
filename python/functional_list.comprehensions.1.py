
squared = [x ** 2 for x in range(4)]
for i in squared:
    print i

sqdEvens = [x ** 2 for x in range(8) if not x % 2]
for i in squared:
    print i

map(lambda x: x ** 2, range(6))
[x ** 2 for x in range(6)]

filter(lambda x: x % 2, seq)
[x for x in seq if x % 2]
[(x+1,y+1) for x in range(3) for y in range(5)]
