
#include <iostream>

class A {
	public:
		int a1;
	protected:
		int a2;
	private:
		int a3;
	public:
		friend B;
};

class B {

};

using namespace std;

int main(int argc, char** arg) {
	B ob;
	ob.a1 = 1;
}

