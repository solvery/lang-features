
#include <iostream>

using namespace std;

class A{
	public:
		friend void foo();
};

void foo(){
	cout << "hello" << endl;
}

int main(int argc, char** arg) {
	foo();
}

