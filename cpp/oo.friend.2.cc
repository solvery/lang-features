
#include <iostream>

class A {
	public:
		int a1;
	protected:
		int a2;
	private:
		int a3;
};

class B {
	public:
		friend A;

};

using namespace std;

int main(int argc, char** arg) {
	B ob;
	ob.a1 = 1;
}

