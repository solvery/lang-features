
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


