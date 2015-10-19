// static_cast没有运行时的开销。
// 多态类型转换，使用dynamic_cast可以进行运行时检查。
//  
#include <iostream>
using namespace std;

class A {};
class B : public A {};
class C : public A {};


int main(int argc, char** arg) {
	{
		double d = 3.14;
		int i = static_cast<int>(d);
	}
	A* p = new B();
	//B* pb = dynamic_cast<B*>(pa);
	B* pb = static_cast<B*>(p);
}

