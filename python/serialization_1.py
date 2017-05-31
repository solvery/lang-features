import pickle 

d = dict(name='Bob', age=20, score=98)
s = pickle.dumps(d)
d1 = pickle.loads(s)
print (d1)
