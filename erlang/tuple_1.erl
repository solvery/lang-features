% 

-module(tuple_1).
-export([start/0]).

start() ->
	Point = {point, 1, 2},
	{point, X, Y} = Point, 
    io:format("~p~n", [[X, Y]]),
    io:format("~p~n", [0]),
    io:format("~n").

