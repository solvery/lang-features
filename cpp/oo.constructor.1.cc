// default constructor
// constructor initializer list

#include <iostream>

using namespace std;

class A {
	public:
		int v1;
		int v2;
		string s1;
		A(): v1(1), v2(2) { }
		A(const string &s): s1(s), v1(3), v2(4) { }
};

class B {
	public:
		int v1;
		int v2;
		A() {
			v1 = 1;
			v2 = 2;
		}
}

int main(int argc, char** arg) {
	A oa1;
	A oa2("hello");
	cout << oa1.v1 << endl;
	cout << oa2.v1 << endl;
	cout << oa2.s1 << endl;
}

