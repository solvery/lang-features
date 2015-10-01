#include <iostream>
#include <typeinfo>

class Base {virtual void Member(){}};
class Derived : Base {};

int main ()
{
	try {
		Base b;
		Derived& rd = dynamic_cast<Derived&>(b);
	} catch (std::bad_cast& bc) {
		std::cerr << "bad_cast caught: " << bc.what() << std::endl;
	}
	return 0;
}
