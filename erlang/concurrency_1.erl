% 

-module(concurrency_1).
-export([start/0]).

start() ->
    io:format("~p~n", [0]),
    io:format("~n").

