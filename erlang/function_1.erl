% 函数由子句构成
% 选择子句
% 分号（;）分隔子句
% when 子句保护式
% case
% if 

-module(function_1).
-export([start/0]).

start() ->
    io:format("~s~n",[either_or_both_1(hehe,true)]),
    io:format("~s~n",[either_or_both_1(false,hehe)]),
    io:format("~s~n",[either_or_both_2(true,true)]),
    io:format("~s~n",[either_or_both_3(true,true)]),

    io:format("~f~n", [area_1({circle, 10})]),
    io:format("~f~n", [area_2({circle, 10})]),

    io:format("~s~n", [sign(2)]),
    io:format("~s~n", [sign(-2)]),

    %io:format("~s~n", []),
    io:format("~n").

% pattern match
either_or_both_1(true, _)		-> true;
either_or_both_1(_, true)		-> true;
either_or_both_1(false, false)	-> false;
either_or_both_1(_, _)			-> false.

either_or_both_2(true, B) when is_boolean(B)	-> true;
either_or_both_2(A, true) when is_boolean(A)	-> true;
either_or_both_2(false, false)					-> false.

% case 
either_or_both_3(A,B) -> 
	case {A,B} of 
		{_,true}	-> true;
		{true,_}	-> true;
		{flase,flash} -> flase
	end.

area_1({circle, Radius})	-> Radius * Radius * math:pi();
area_1({square, Side})	-> Side * Side;
area_1({rectangle, Height, Width})	-> Height * Width.

area_2(Shape) ->
    case Shape of
        {circle, Radius} ->
            Radius * Radius * math:pi();
        {square, Side} ->
            Side * Side;
        {rectangle, Height, Width} ->
            Height * Width
    end.

% if 
sign(N) when is_number(N) ->
    if
       N > 0 -> positive;
       N < 0 -> negative;
       true  -> zero
    end.



