
#include <iostream>

using namespace std;

class A
{
	public:
		virtual void func()
		{
			cout << "A func"<< endl;
		}
};

class B : public  A
{
	public:
		void func()
		{
			cout << "B func" << endl;
		}
};
int main(int argc, char** arg) {

	A* a ;
	A aa;
	B bb;
	//a= &aa;
	a=&bb;
	a->func();
}

