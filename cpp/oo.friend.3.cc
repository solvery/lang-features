
#include <iostream>

using namespace std;

class A{
		friend class B;
	public:
		void m1();

};

void A::m1() {
	cout << "hello" << endl;
}

class B {
	public:
		void foo (){
			A::m1();
		}
};

int main(int argc, char** arg) {
	B b;
	b.foo();
}

