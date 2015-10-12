// 模板的模板参数

#include <iostream>
using namespace std;

/// template <template <typename T> typename U>
template <typename S, template <typename T> class U>
class A {
	public:
		U<S> v2;
};

int main(int argc, char** arg) {
}

