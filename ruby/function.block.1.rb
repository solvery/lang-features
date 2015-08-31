
# Ruby简直就是个代码块的大联欢

# {}
3.times {print "Ruby! "}
3.times { |x| puts "Ruby!"}

# 用yield调用代码块
# 开放类, class关键字会定义一个类，但如果该类已定义过，再调用class会 修改先前的类定义
class Fixnum
    def my_times
        i = self 
        while i>0
            i = i - 1
            yield
        end
    end
end
puts
3.my_times {print "Ruby! "}

# 代码块用作一等参数（first-class parameter）
# “&”，表示将代码块作为闭包传递给函数
def call_block(&block)
    block.call
end

def pass_block(&block)
    call_block(&block)
end

puts
pass_block {puts 'Hello, block'}

