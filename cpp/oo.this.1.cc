
#include <iostream>

using namespace std;

class A {
	private:
		int v1;
	public:
		A& m1(int a){
			this->v1 = a;
			return *this;
		}
};

int main(int argc, char** arg) {
}

