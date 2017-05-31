#encoding=utf-8

import hashlib

m = hashlib.md5()
# 每调用一次update(s)，相当于给md5对象m增加了s。对一个新的需md5加密的内容，需要新建一个md5对象。    
m.update(b'hello')
print m.hexdigest()
