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


