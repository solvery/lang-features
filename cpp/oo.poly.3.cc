
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
		void foo() {
			cout << "B foo" << endl;
		}
};

int main(int argc, char** arg) {

	A* pa ;
	B* pb ;
	A oa;
	B ob;
	pa=&oa;
	pa->foo();
	pa=&ob;
	pa->foo();

	pa=&oa;
	pa->bar(pa);
	pa=&ob;
	pa->bar(pa);
}

