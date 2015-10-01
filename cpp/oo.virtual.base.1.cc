
#include <iostream>

using namespace std;

class A {
	public:
		A(){
			cout << "A()" << endl;
		}
};

class B : public A {
	public:
		B(){
			cout << "B()" << endl;
		}
};

class C : public A {
	public:
		C(){
			cout << "C()" << endl;
		}
};

class D : public B,C {
	public:
		D(){
			cout << "D()" << endl;
		}
};

int main(int argc, char** arg) {
	D od;
}

