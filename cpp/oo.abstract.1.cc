// abstract class

#include <iostream>

using namespace std;

class A {
	public:
		virtual void foo()=0; // 纯虚函数，抽象类，不能实例化。
};

class B : public A {
	// 未定义基类中的纯虚函数，任然是抽象类。
};

class C : public B {
	public:
		void foo(){}
};


int main(int argc, char** arg) {
	/// A oa;
	/// B ob;
	C oc;
}


