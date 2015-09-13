% for 

-module(function_3).
-export([start/0]).

start() ->
	io:format("~p~n", [for(1,10,fun(I) -> I end)]),
    io:format("~p~n", [fib1(20)]),
    io:format("~p~n", [fib2(20)]),
    io:format("~n").

for(Max, Max, F) -> [F(Max)];
for(I, Max, F)   -> [F(I)|for(I+1, Max, F)].

fib1(0) -> 1;
fib1(1) -> 1;
fib1(N) -> fib1(N-1) + fib1(N-2).

fib2(N) -> fib2(N, 1, 1).
fib2(0, A, _) -> A;
fib2(N, A, B) -> fib2(N-1, B, A+B).

