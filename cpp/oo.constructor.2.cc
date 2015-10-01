// copy constructor

#include <iostream>

using namespace std;

class A {
	public:
		int v1;
		A(): v1(1) {}
		// build in copy constructor.
};

class B {
	public:
		int v1;
		B(): v1(1) {}
		B(const B& a) {
			v1 = a.v1;
		}
};

class C {
	public:
		int v1;
		C(): v1(1) {}
		C(const C& a);
};

int main(int argc, char** arg) {
	{
		A o1;
		o1.v1 = 2;
		A o2(o1);
		A o3 = o1;
		cout << o2.v1 << endl;
		cout << o3.v1 << endl;
	}
	{
		B o1;
		o1.v1 = 2;
		B o2(o1);
		B o3 = o1;
		cout << o2.v1 << endl;
		cout << o3.v1 << endl;
	}
	{
		C o1;
		o1.v1 = 2;
		/// C o2(o1);
		/// C o3 = o1;
	}
}

