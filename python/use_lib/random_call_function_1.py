import random

def f1():
    print "f1"

def f2():
    print "f2"

function_list = [f1,f2]

for i in range(1,5):
    random.choice(function_list)()
