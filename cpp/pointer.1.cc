#include <iostream>

// 空指针调用静态函数
class Foo {
	public:
		// static void bar() {
		void bar() {
			std::cout << "bar()" << std::endl;
		}
};

int main(void) {
	Foo * foo = NULL;
	foo->bar(); //=> WTF!?
	return 0; // Ok!
}

