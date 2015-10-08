
#include <iostream>
#include <algorithm>
#include <numeric>
#include <string>
#include <vector>

using namespace std;

class Base {
    public:
        virtual void f() { cout << "Base::f" << endl; }
        virtual void g() { cout << "Base::g" << endl; }
        virtual void h() { cout << "Base::h" << endl; }

};

int main(int argc, char** arg) {
    typedef void(*Fun)(void);

    Base b;
    

    Fun pFun = NULL;

    cout << "addr vtable: \t\t\t" << (long*)(&b) << endl;

    // Invoke the first virtual function 
    pFun = (Fun)*((int*)*(int*)(&b));
    cout << "addr vtable function 1: \t" << &pFun << endl;
    pFun();
}

