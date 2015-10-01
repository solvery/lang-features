
#include <iostream>

using namespace std;

class A {
	public:
		virtual void foo() {
			cout << "A foo"<< endl;
		}
		void bar(A *pa) {
			pa->foo();
		}
};

class B : public  A {
	public:
		void foo() {  // is virtual 
			cout << "B foo" << endl;
		}
};

class C : public  B {
	public:
		void foo() { // is virtual
			cout << "C foo" << endl;
		}
};

int main(int argc, char** arg) {

	A* pa ;

	A oa;
	B ob;
	C oc;
	pa=&oa;
	pa->foo();
	pa=&ob;
	pa->foo();
	pa=&oc;
	pa->foo();

	pa=&oa;
	pa->bar(pa);
	pa=&ob;
	pa->bar(pa);
}

