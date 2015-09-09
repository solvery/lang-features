-module(basic_2).
-export([start/0]).

start() ->
	42,
	101,
	-101,
	1234567890 * 9876543210 * 999999999,
	
	16#abcdef,
	2#1010,
	
	3.14,
	-0.1234,
	5.22e23,
	6.667e-11,
	
	% 
	<<0, 1, 2>>,
	<<"hello", 32, "dude">>,

	% atom, symbol in lisp.
	ok,
	error,
	foo,
	route66,
	atoms_oftem_con,
	at@at,
	'$!@#$!',
	'Upcase',
	'With space\n',

	% tuple
{1, 2, 3},
{one, two, three},
{from, "Russia", "with love"},
{complex, {nested, "structure", {here}}},
{},

	% list
	[],
	[1,2,3],
	[one, two, three],
	[[1,2,3], [4,5,6]],
	[{tomorrow, "buy cheese"},
	 {soon, "fix trap door"},
	 {later, "repair moon rocket"}],
	% 
	[1 | []],
	[2 | [1]],
	[5,4,3 | [2,1]],
	%
	[1,2,3,4] ++ [],

	% string
	"abcd",
	"Hello",
	" \r\t\n",
	"",

	%% pid, port, reference
	%% compare
	1 < 2,
	1 > 2,
	1 =< 2,
	1 >= 2,
	1 =:= 1,
	1 =/= 1,
	1 =:= 1.0,
	1 == 1.0,
	1 /= 1.0,

	%% call function
	lists:reverse([12,3,4])
	.
