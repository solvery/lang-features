#include <iostream>

using namespace std;
using std::string;

class C;
class D;

class A {
	public:
		string show(D* obj) { return ("1 A and D"); }
		string show(A* obj) { return ("2 A and A"); }
};

class B : public A {
	public:
		string show(B* obj) { return ("3 B and B"); }
		string show(A* obj) { return ("4 B and A"); }
};
class C : public B {};
class D : public B {

};

int main(int argc, char** arg) {

	A oa;
	B ob;
	C oc;
	D od;
	A* pa = &oa;
	B* pb = &ob;
	C* pc = &oc;
	D* pd = &od;

	A* a1 = &oa;
	A* a2 = &ob;

	cout << pa->show(pb) << endl;
	cout << pa->show(pc) << endl;
	cout << pa->show(pd) << endl;
	cout << pb->show(pb) << endl;
	cout << pb->show(pc) << endl;
	cout << pb->show(pd) << endl;
	cout << pb->show(pb) << endl;
	cout << pb->show(pc) << endl;
	cout << pb->show(pd) << endl;
	cout << "" << endl;
	cout << a1->show(pb) << endl;
	cout << a1->show(pc) << endl;
	cout << a1->show(pd) << endl;
	cout << a2->show(pb) << endl;
	cout << a2->show(pc) << endl;
	cout << a2->show(pd) << endl;
	cout << pb->show(pb) << endl;
	cout << pb->show(pc) << endl;
	cout << pb->show(pd) << endl;
	cout << "" << endl;
	return 0;
}

