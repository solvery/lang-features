% build-in function.
% gurd

-module(bif_1).
-export([start/0]).

start() ->
    io:format("~p~n", [list_to_tuple([1,2,"hehe"])]),
    io:format("~p~n", [0]),
    io:format("~n").

