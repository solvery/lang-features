
aList=[]
    
try:
    try:
        aList[1]
    #except BaseException, e:
    except Exception, e:
        print e
finally:
    print 'hehe'

# raise
# assert 
assert 2 + 2 == 2 * 2
