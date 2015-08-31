#!/usr/bin/env ruby
#
# vim:syntax=ruby:sw=4:ts=4:expandtab

# to_s在模块中使用，在类中实现
# 类似于Java里面的接口, 依赖关系是隐式的，通过鸭子类型来实现。
# 混入（mix in） 
# 先定义类的主要部分，然后用模块添加额外功能

module ToFile
    def filename
        "object_#{self.object_id}.txt"
    end

    def to_f
        #File.open(filename, 'w') {|f| f.write(to_s)}
        puts to_s
    end
end

class Person
    include ToFile
    attr_accessor :name

    def initialize(name)
        @name = name
    end

    def to_s
        name
    end
end

Person.new("matz").to_f
