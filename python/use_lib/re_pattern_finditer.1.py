# encoding: UTF-8 
import re
 
# 搜索string，返回一个顺序访问每一个匹配结果（Match对象）的迭代器。
p = re.compile(r'\d+')
for m in p.finditer('one1two2three3four4'):
    print m.group(),
