
#include <iostream>

using namespace std;

class A {
	friend class B;
	enum {a=1};
};

class B {
	int v[A::a];
};


int main(int argc, char** arg) {
}

