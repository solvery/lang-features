#include <iostream>
#include <typeinfo>

class A {virtual void m1(){}};

int main ()
{
	try {
		A * pb = 0;
		std::cout << typeid(*pb).name();
	} catch (std::bad_typeid& e) {
		std::cerr << "bad_typeid caught: " << e.what() << std::endl;
	}
	return 0;
}
