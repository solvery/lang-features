# encoding: UTF-8 
import re
 
# 按照能够匹配的子串将string分割后返回列表
p = re.compile(r'\d+')
print p.split('one1two2three3four4')

p = re.compile(r'\D+')
print p.split('one1two2three3four4')
