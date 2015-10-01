
#include <iostream>

using namespace std;

class A{
	public:
		friend class B;
		void m1() {
			cout << "A m1()" << endl;
		}
	private:
		void m2() {
			cout << "A m2()" << endl;
		}

};

class B {
	public:
		void foo (){
			a.m1();
			a.m2();
		}
	private:
		A a;

};

int main(int argc, char** arg) {
	B b;
	b.foo();
	/// b.m1();
}

