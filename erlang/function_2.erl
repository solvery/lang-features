% fun

-module(function_2).
-export([start/0]).

start() ->
	Double = fun(X) -> 2.0*X end,
    io:format("~f~n", [Double(2)]),

	% fun as args
	L1 = [1,2,3,4],
    io:format("~p~n", [lists:map(fun(X) -> 2*X end, L1)]),
    io:format("~p~n", [lists:filter(fun(X) -> (X rem 2) =:= 0 end, L1)]),

	Even = fun(X) -> (X rem 2) =:= 0 end,
    io:format("~p~n", [lists:map(Even, L1)]),
    io:format("~p~n", [lists:filter(Even, L1)]),

	% fun as return
	MakeTest = fun(L) -> (fun(X) -> lists:member(X,L) end) end,
	IsInList = MakeTest(L1),
    io:format("~p~n", [IsInList(1)]),
    io:format("~p~n", [IsInList(8)]),
    io:format("~p~n", [lists:filter(IsInList, [1,3,4,5,6,7])]),

    io:format("~n").


