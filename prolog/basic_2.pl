% without keyword: if, case.
% assignment
% , ; ?? ??
% =:= \= < > =< >=
% + - * / // mod

basic_2 :-
	format('hehe~n'),
	X = 3,
	4 = Y,
	(X, Y) = (1, 2),
	[X, Y] = [1, 2],
	{X, Y} = {1, 2},
	foo(X, Y) = foo(1, 2),
	true, 
	fail,
	is(X, 2 + 2),
	format('~p~n', ['aa']),
	format('hehe~n'),
	halt.

