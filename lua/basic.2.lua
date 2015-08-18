
-- variable
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

-- while
sum = 0
num = 1
while num <= 100 do
    sum = sum + num
    num = num + 1
end
print("sum =",sum)

-- if else
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

-- for
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

-- function
sum = 2
repeat
   sum = sum ^ 2 --幂操作
   print(sum)
until sum >1000

function fib(n)
  if n < 2 then return 1 end
  return fib(n - 2) + fib(n - 1)
end

-- multi return value
name, age, bGay = "haoel", 37, false, "haoel@hotmail.com"

function getUserInfo(id)
    print(id)
    return "haoel", 37, "haoel@hotmail.com", "http://coolshell.cn"
end

name, age, email, website, bGay = getUserInfo()

function foo(x) return x^2 end
foo = function(x) return x^2 end

-- table, key - value pair
haoel = {name="ChenHao", age=37, handsome=True}
haoel.website="http://coolshell.cn/"
local age = haoel.age
haoel.handsome = false
haoel.name=nil

t = {[20]=100, ['name']="ChenHao", [3.14]="PI"} 
for k, v in pairs(t) do
    print(k, v)
end


-- array
arr = {10,20,30,40,50}
arr = {[1]=10, [2]=20, [3]=30, [4]=40, [5]=50}
arr = {"string", 100, "haoel", function() print("coolshell.cn") end}
for i=1, #arr do
    print(arr[i])
end

