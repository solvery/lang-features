
a,b=1,2
x,y,z=[1,2,3]
# 3 is discarded:
x, y = 1, 2, 3
x, y, z = 1, 2
x, y = y, x

13.to_f / 5
13.fdiv(5)

# global var
$g1, $g2 = 7, 8
def swap_globals
    $g1, $g2 = $g2, $g1
end

swap_globals()
puts $g1, $g2
