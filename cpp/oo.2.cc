#include <iostream>

using namespace std;

class A {
	public:
		int v1;
		void m1(){ cout << "A m1()" << endl; }
	protected:
		int v2;
		void m2(){ cout << "A m2()" << endl; }
	private:
		int v3;
		void m3(){ cout << "A m3()" << endl; }

	public:
		A(){
			v1=1;
			v2=2;
			v3=3;
		}

		void m4();
};

void A::m4(){
	cout << "A m4()" << endl;
}

class B1 : public A {
	public:
		void b1m1() {
			cout << A::v1 << endl;
			cout << A::v2 << endl;
			/// cout << A::v3 << endl;
		}
	protected:
		void b1m2() {
			cout << A::v1 << endl;
			cout << A::v2 << endl;
			/// cout << A::v3 << endl;
		}
	private:
		void b1m3() {
			cout << A::v1 << endl;
			cout << A::v2 << endl;
			/// cout << A::v3 << endl;
		}
};

int main(int argc, char** arg) {
	{
	}
}


