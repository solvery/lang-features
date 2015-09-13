// generic

#include <iostream>

using namespace std;

// type
template <class A>
class Foo {
	public:
		A a;
		Foo(A a);
};

template <class A>
Foo<A>::Foo(A a) : a(a) {
}

// function
template <class C>
C add(C a, C b) {
	return a + b;
}

// array
template <class C>
class Foo2 {
	public:
		C a[10];
};

// args
template <int N>
int add(int i) {
	return N+i;
}

template <class A, class B>
class Pair {
	public:
		A a;
		B b;
		Pair(A a, B b);
};

template <class A, class B>
Pair<A, B>::Pair(A a, B b) :
	a(a), b(b) { };

int main(int argc, char** arg) {
	{
		Foo<string> f = Foo<string>("foo");
	}
	{
		cout << add<7>(3) << endl;
	}
	{
		Pair<int, string> p =
			Pair<int, string>(7, "foo");
	}
	{

		Pair<int, Foo<string> > p =
			Pair<int, Foo<string> >(
					7, Foo<string>("foo"));

	}
	{
	}
}


