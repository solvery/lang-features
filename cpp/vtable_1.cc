
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
    pFun = (Fun)*((long*)*(long*)(&b));

    pFun = (Fun)*((long*)*(long*)(&b)+0);
    pFun();

    pFun = (Fun)*((long*)*(long*)(&b)+1);
    pFun();

    pFun = (Fun)*((long*)*(long*)(&b)+2);
    pFun();

    cout << "addr vtable function 1: \t" << ((long*)*(long*)(&b)+0) << endl;
    cout << "addr vtable function 2: \t" << ((long*)*(long*)(&b)+1) << endl;
    cout << "addr vtable function 3: \t" << ((long*)*(long*)(&b)+2) << endl;
}

