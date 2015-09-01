
# sinleton

Highlander := Object clone
# 重定义了clone方法，让它返回Highlander对象自身
Highlander clone := Highlander
a1 := Highlander clone
a2 := Highlander clone
a1 == a2

b1 := Object clone 
b2 := Object clone 
b1 == b2
