-module(basic_3).
-export([start/0]).

start() ->
	X = 17,
	X1 = X + 1,
	
{A,B,C} = {1970, "Richard", male},
{rectangle, Width, Hight} = {rectangle, 200, 100},

	Users = [{person, [{name, "Martin", "Logan"}, {shoe_size, 12},
	{tags, [jujitsu, beer, erlang]}]}],
	[ {person, [{name,_,Surname},_,{tags,Tags}]} | _] = Users,

	[1,2,3 | Rest] = [1,2,3,4,5,6,7],
	[$h,$t,$t,$p,$: | Site1] = """http://www.hehe.com",
	"http://" ++ Site2 = "http://www.hehe.com",


