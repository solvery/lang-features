#!/usr/local/bin/io

4<5
4<=3

true and false
true and true
true or true
4<5 and 6>7
true and 0 # 0 is true

# true、false和nil都是单例
# 对它们进行复制，返回的只是单例对象的值
true proto 
true clone
false clone
nil clone

# loop()

i := 1
while(i<5, i println; i=i+1); "hehe" println
for(i, 1, 5, i println); "hehe" println
for(i, 1, 10, 2, i println); "hehe" println

for(i, 1,2,1, i println, "extra argument")
for(i, 1,2,   i println, "extra argument") # error

# if(condition, true code, false code)
if(true, "hehe", "haha")
if(false) then("hehe") else("haha")
if(false) then("hehe" println) else("haha" println)

