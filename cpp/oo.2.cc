#include <iostream>

using namespace std;

class A {
	private:
		int v1;
		void m1(){ cout << "A m1()" << endl; }
	protected:
		int v2;
		void m2(){ cout << "A m2()" << endl; }
	public:
		int v3;
		void m3(){ cout << "A m3()" << endl; }

		void m2();
};

void A::m2(){
	cout << "A m2()" << endl;
}

class B1 : public A {
	public:
		void b1m1() {
			m1();
			m2();
			m3();
		}
	protected:
	public:
};

int main(int argc, char** arg) {
	{
	}
}


