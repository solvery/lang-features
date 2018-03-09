#encoding=utf-8

import hashlib
import sys

key=sys.argv[1]
m = hashlib.md5()
m.update(key)
m.update(m.hexdigest())
print key, m.hexdigest()[:5]
