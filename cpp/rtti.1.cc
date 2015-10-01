#include <iostream>
using namespace std;

struct Base {
	virtual ~Base() {}
	virtual char Type() const = 0;
};

struct A : public Base {
	char Type() const {
		return 'A';
	}
};

struct B : public Base {;
	char Type() const {
		return 'B';
	}
};

int main() {
	Base * bp = new A;
	int n = 0;
	for ( int i = 0; i < 10000000; i++ ) {
#define RTTI
#ifdef RTTI
		if ( A * a = dynamic_cast <A*> ( bp ) ) {
			n++;
		}
#else
		if ( bp->Type() == 'A' ) {
			A * a = static_cast <A*>(bp);
			n++;
		}
#endif
	}
	cout << n << endl;
}
