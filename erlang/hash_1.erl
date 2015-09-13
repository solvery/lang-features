% record, map 

-module(hash_1).
-export([start/0]).

-record(todo, {status=reminder,who=joe, text}).

start() ->
	#todo{},
	X1 = #todo{status=urgent, text="Fix something."},
	X2 = X1#todo{status=done},
    io:format("~p~n", [X2]),
    io:format("~p~n", [0]),
    io:format("~n").

