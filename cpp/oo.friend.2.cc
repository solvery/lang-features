
#include <iostream>

class A {
	friend class B;
};

class B {
};

using namespace std;

int main(int argc, char** arg) {
	B ob;
}

