% list

-module(list_1).
-export([start/0]).

start() ->
    io:format("~p~n", [sum([1,2,3,4])]),
    io:format("~p~n", [0]),
    io:format("~n").

map(_, [])     -> [];
map(F,  [H|T]) -> [F(H)|map(F, T)].

member(H, [H|_]) -> true;
member(H, [_|T]) -> member(H, T);
member(_, [])    -> false.
    
sum([H|T]) -> H + sum(T);
sum([])    -> 0.

partition(Pred, L) -> partition(Pred, L, [], []).

partition(Pred, [H|T], Ts, Fs) ->
    case Pred(H) of
	true  -> partition(Pred, T, [H|Ts], Fs);
	false -> partition(Pred, T, Ts, [H|Fs])
    end;
partition(_, [], Ts, Fs) ->
    {reverse(Ts), reverse(Fs)}.
%END:partition

reverse(L) -> reverse(L, []).

reverse([H|T], L) -> reverse(T, [H|L]);
reverse([], L)    -> L.

