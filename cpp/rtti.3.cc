#include <typeinfo>
#include <iostream>

class Base1 { public: virtual void func1(){} };
class Base2 { public: virtual void func2(){} };

class D:public Base1, public Base2 {};

int main()
{
	Base1 * b1 = new D;
	Base2 & b2 =  dynamic_cast<Base2&>(*b1);

	std::cout << "Base1 " << uintptr_t(b1) <<" " << typeid(*b1).name() << std::endl
		<< "Base2 " << uintptr_t(&b2) << " " <<typeid(b2).name() << std::endl;

	return 0;
}

