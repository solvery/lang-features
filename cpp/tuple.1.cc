#include <iostream>
#include <tuple>

using namespace std;

int main(int argc, char** arg) {
	{
		tuple<string, int, float> tup("foo", 1, 3.7);
		tuple<string, int, float> tup2;
		auto tup3 = make_tuple("foo", 1, 3.7);
	}
	{
		tuple<string, int, float> tup("foo", 1, 3.7);

		string s = get<0>(tup);
		int i = get<1>(tup);
		float x = get<2>(tup);
	}
	{
		tuple<string, int, float> tup("foo", 1, 3.7);
		string s;
		float x;

		tie(s, ignore, x) = tup;
		get<0>(tup) = "bar";
		tuple_size<decltype(tup)>::value;
	}
	{
		pair <string, int> p2("foo", 7);
		pair <string, int> p1;
		//element types are inferred:
		auto p3 = make_pair("foo", 7);
	}
	{
		auto p = make_pair("foo", 7);
		string s = p.first;
		int i = p.second;
		p.first = "bar";
		p.second = 8;
	}
	{
	}
}


