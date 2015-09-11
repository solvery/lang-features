% list comprehension
% ||, <-

-module(list_2).
-export([start/0]).

start() ->
	L1 = [1,2,3,4],
    io:format("~p~n", [[X*2 || X <- L1]]),

	L2 = [{a,1},{b,2},{c,3}],
    io:format("~p~n", [ [{C,2*N} || {C,N} <- L2 ] ]),

	L3 = [23,6,2,9,27,400,78,45,61,14],
    io:format("~p~n", [qsort(L3)]),

    io:format("~p~n", [pythag(30)]),

    io:format("~p~n", [perms("abc")]),
    io:format("~p~n", [0]),

    io:format("~n").

qsort([]) -> [];
qsort([Pivot|T]) ->
	qsort([X || X <- T, X < Pivot])
	++ [Pivot] ++
	qsort([X || X <- T, X >= Pivot]).

pythag(N) ->
    [ {A,B,C} ||
        A <- lists:seq(1,N),
        B <- lists:seq(1,N),
        C <- lists:seq(1,N),
        A+B+C =< N,
        A*A+B*B =:= C*C 
    ].

perms([]) -> [[]];
perms(L)  -> [[H|T] || H <- L, T <- perms(L--[H])].

