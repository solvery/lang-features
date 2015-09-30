#include <iostream>

using namespace std;
using std::string;

class C;
class D;

class A {
	public:
	   	string show(D obj) { return ("1 A and D"); }
    	string show(A obj) { return ("2 A and A"); }
};

class B : public A {
	public:
		string show(B obj) { return ("3 B and B"); }
		string show(A obj) { return ("4 B and A"); }
};
class C : public B {};
class D : public B {};

int main(int argc, char** arg) {
	{
	}
}


