% for 

-module(function_3).
-export([start/0]).

start() ->
	io:format("~p~n", [for(1,10,fun(I) -> I end)]),
    io:format("~n").

for(Max, Max, F) -> [F(Max)];
for(I, Max, F)   -> [F(I)|for(I+1, Max, F)].

