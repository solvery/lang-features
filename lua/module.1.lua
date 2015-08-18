
require("hello")
require("hello") -- not load again

dofile("hello.lua") -- execute every time

local hello = loadfile("hello.lua") -- execute later
hello()

