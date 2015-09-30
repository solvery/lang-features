#include <iostream>

using namespace std;

class A {
	public:
		int v1;
	protected:
		int v2;
	private:
		int v3;

	public:
		A(){
			v1=1;
			v2=2;
			v3=3;
		}
		void show() {
			cout << v1 << '\t';
			cout << v2 << '\t';
			cout << v3 << '\t' << endl;
		}
};

class B1 : public A {};
class B2 : protected A {};
class B3 : private A {};

int main(int argc, char** arg) {
	A oa;
	B1 ob1;
	B2 ob2;
	B3 ob3;
	oa.v1 = 1;
	/// oa.v2 = 1;
	/// oa.v3 = 1;
	/// ob3.v1 = 1;
	/// ob3.v2 = 1;
	/// ob3.v3 = 1;
}




