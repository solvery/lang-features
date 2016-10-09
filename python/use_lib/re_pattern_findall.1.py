# encoding: UTF-8 
import re
 
# 搜索string，以列表形式返回全部能匹配的子串。 
p = re.compile(r'\d+')
print p.findall('one1two2three3four4')
