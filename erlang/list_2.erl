% list

-module(list_2).
-export([start/0]).

start() ->
	L1 = [1,2,3,4],
    io:format("~p~n", [2*X || X <- L1]),
    io:format("~p~n", [0]),
    io:format("~n").

