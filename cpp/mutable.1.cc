// 属性修饰为mutable, 这样可以在const修饰的方法中可修改。

#include <iostream>

using namespace std;

class A {
	public:
		A(): v1(0) {}
		void show() const {
			cout << v1 << endl;
			v1++;
		}
	private:
		/// int v1;
		mutable int v1;
};

int main(int argc, char** arg) {
	A oa1;
	oa1.show();
	oa1.show();
}


