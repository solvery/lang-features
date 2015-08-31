
3.times {print "Ruby! "}
puts
1.upto(5) { |x| print x }
puts

a = [1,2,3,4]
a.each do |i|
    print i 
end
puts
b=a.map {|x| x*x}
c=a.select {|x| x%2==0}
a.inject do |sum, x|
    sum + x
end
puts a.inject
