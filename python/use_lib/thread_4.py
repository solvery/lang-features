#!/usr/bin/python
import threading
import time
 
def worker(id):
    print "worker %d %s" % (id, time.ctime())
    time.sleep(1)
    return
 
for i in xrange(5):
    t = threading.Thread(target=worker, args=(i,))
    t.start()
