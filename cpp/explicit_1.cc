// 通过将构造函数声明为 explicit，来防止在需要隐式转换的上下文中使用构造函数：

#include <iostream>

using namespace std;

class A {
    public:
        A() {}
        explicit A(int a): v1(a)  {
        }
    private:
        int v1;
};

int main(int argc, char** arg) {
    A oa1;
    /// A oa2 = 2;
    A oa3 = A(2);
    A oa4(3);
}


