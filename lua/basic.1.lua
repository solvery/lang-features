-- 两个减号是行注释
 

--[[
 这是块注释
 这是块注释
 --]]

print("Hello World")

num = 1024
num = 3.0
num = 3.1416
num = 314.16e-2
num = 0.31416E1
num = 0xff
num = 0x56

a = 'alo\n123"'
a = "alo\n123\""
a = '\97lo\10\04923"'
a = [[alo
123"]]

v = UndefinedVariable
theGlobalVar = 50
local theLocalVar = "local variable"

sum = 0
num = 1
while num <= 100 do
    sum = sum + num
    num = num + 1
end
print("sum =",sum)

if age == 40 and sex =="Male" then
    print("男人四十一枝花")
elseif age > 60 and sex ~="Female" then
    print("old man without country!")
elseif age < 20 then
    io.write("too young, too naive!\n")
else
    local age = io.read()
    print("Your age is "..age)
end

sum = 0
for i = 1, 100 do
    sum = sum + i
end
 

sum = 0
for i = 1, 100, 2 do
    sum = sum + i
end
 

sum = 0
for i = 100, 1, -2 do
    sum = sum + i
end


sum = 2
repeat
   sum = sum ^ 2 --幂操作
   print(sum)
until sum >1000

function fib(n)
  if n < 2 then return 1 end
  return fib(n - 2) + fib(n - 1)
end

-- 闭包
function newCounter()
    local i = 0
    return function()     -- anonymous function
       i = i + 1
        return i
    end
end

c1 = newCounter()
print(c1())  --> 1
print(c1())  --> 2

function myPower(x)
    return function(y) return y^x end
end

power2 = myPower(2)
power3 = myPower(3)

print(power2(4)) --4的2次方
print(power3(5)) --5的3次方

name, age, bGay = "haoel", 37, false, "haoel@hotmail.com"

function getUserInfo(id)
    print(id)
    return "haoel", 37, "haoel@hotmail.com", "http://coolshell.cn"
end

name, age, email, website, bGay = getUserInfo()

function foo(x) return x^2 end
foo = function(x) return x^2 end

-- table
haoel = {name="ChenHao", age=37, handsome=True}
haoel.website="http://coolshell.cn/"
local age = haoel.age
haoel.handsome = false
haoel.name=nil

t = {[20]=100, ['name']="ChenHao", [3.14]="PI"} 

-- array
arr = {10,20,30,40,50}
arr = {[1]=10, [2]=20, [3]=30, [4]=40, [5]=50}
arr = {"string", 100, "haoel", function() print("coolshell.cn") end}
for i=1, #arr do
    print(arr[i])
end

-- Lua也是用Table来管理全局变量的，Lua把这些全局变量放在了一个叫“_G”的Table里。
_G.globalVar
_G["globalVar"]
for k, v in pairs(t) do
    print(k, v)
end

-- MetaTable 和 MetaMethod
fraction_a = {numerator=2, denominator=3}
fraction_b = {numerator=4, denominator=7}
fraction_op={}
function fraction_op.__add(f1, f2)
    ret = {}
    ret.numerator = f1.numerator * f2.denominator + f2.numerator * f1.denominator
    ret.denominator = f1.denominator * f2.denominator
    return ret
end
setmetatable(fraction_a, fraction_op)
setmetatable(fraction_b, fraction_op)
fraction_s = fraction_a + fraction_b


