
x=4
puts x<5
puts x<=4

puts 'hehe' if 0
puts 'hehe' if true
puts 'hehe' if false
puts 'hehe' if nil 

# <=>被人们叫做太空船操作
puts 'begin' <=> 'end'
puts 'same' <=> 'same'

puts
puts true and false
puts true or  false
puts false and true
puts false && "after flase"
#puts false & "after flase"

# 
a = [1,4,3,2,5]
a.sort()
a.any? {|i| i>6}
a.any? {|i| i>4}
a.all? {|i| i>4}
a.all? {|i| i>0}
a.max
a.member?(2)

a.collect {|i| i*i}
a.select {|i| i%2==0}
a.inject {|sum,i| sum+i}
a.inject {|product,i| product*i}

#
a.inject(0) do |sum, i|
    puts "#{sum}, #{i}"
    sum + i
end


x=0
x=x+1 while x<10
x=x-1 until x==1

while x < 10
    x = x + 1
end

