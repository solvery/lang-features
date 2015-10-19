// static_cast没有运行时的开销。
// const_cast 增加或移除const属性。
// dynamic_cast, 多态类型转换，可以进行运行时检查。
//  
#include <iostream>
using namespace std;

class A {};
class B : public A {};
class C : public A {};

int main(int argc, char** arg) {
	{
		double d = 3.14;
		int i = static_cast<int>(d);
	}
	{
		const char *s1 = "hello";
		char *s2 = const_cast<char*>(s1);
		const char *s3 = const_cast<const char *>(s2);
	}
	{
		int a = 10;
		float f = 10;
		struct NUM {
			int v1;
		};

		/// NUM m = reinterpret_cast<NUM>(a);
	}
	A* p = new B();
	//B* pb = dynamic_cast<B*>(pa);
	B* pb = static_cast<B*>(p);
}

