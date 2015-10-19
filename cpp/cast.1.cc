//  
#include <iostream>
using namespace std;

class A {};
class B : public A {};
class C : public A {};


int main(int argc, char** arg) {
	A oa = A();
	A* pa = &oa;
	B* pb = dynamic_cast<B*>(pa);
}

