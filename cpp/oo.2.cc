#include <iostream>

using namespace std;

class A {
	private:
		int v1;
	protected:
		int v2;
	public:
		int v3;
		void m1(){
			cout << "A m1()" << endl;
		}
		void m2();
};

void A::m2(){
	cout << "A m2()" << endl;
}

class B1 : public A {
	public:
		/// v1 = 1;
		v2 = 2;
		v3 = 3;
	protected:
	public:
};

int main(int argc, char** arg) {
	{
	}
}


