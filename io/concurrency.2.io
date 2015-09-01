
// acotr
slower := Object clone
faster := Object clone

slower start := method(wait(0.2); writeln("slowly"))
faster start := method(wait(0.1); writeln("quickly"))

slower start; faster start
slower @@start; faster @@start; wait(1)
