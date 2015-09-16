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

int main(int argc, char** arg) {
	{
		Foo<string> f = Foo<string>("foo");
	}
	{
		cout << add<7>(3) << endl;
	}
}


