
#include <iostream>

using namespace std;

class A {
	public:
		static int v1;
		int v2;
		/// A(): v1(1), v2(2) { }
		A(): v2(2) { }
		static void m1() {
		}
};

///
int A::v1 = 0;

int main(int argc, char** arg) {
	A oa;
	A::m1();
	A::v1 = 1;

}

