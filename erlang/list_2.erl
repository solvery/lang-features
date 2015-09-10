% list comprehension
% ||

-module(list_2).
-export([start/0]).

start() ->
	L1 = [1,2,3,4],
    io:format("~p~n", [[X*2 || X <- L1]]),

	L2 = [{a,1},{b,2},{c,3}],
    io:format("~p~n", [ [{C,2*N} || {C,N} <- L2 ] ]),

    io:format("~p~n", [0]),

    io:format("~n").

