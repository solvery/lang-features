
// Unit type = void
def hello() = println("Hello, world!")
hello()
def hello2(): Unit = println("Hello, world!")
hello2()

// return type after argument.
def max(x: Int, y: Int): Int = {
	if (x>y) 
		x
	else 
		y
}

// one line
def max2(x: Int, y: Int): Int = if (x>y) x else y
def max3(x: Int, y: Int) = if (x>y) x else y

var r = max(1,2)
println(r)
r = max2(1,2)
println(r)
r = max3(1,2)
println(r)

