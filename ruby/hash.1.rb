
# use [] 

n = {
    1 => 'one',
    2 => 'two'
}

h = {
    :one => 1,
    :two => 2
}
h[:one]
h[:three]=3

h[1]

h.each do |key, value|
    print "#{value}:#{key}; "
end
puts
