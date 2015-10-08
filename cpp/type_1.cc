// c++11

#include <iostream>
#include <algorithm>
#include <numeric>
#include <string>
#include <vector>

using namespace std;

struct S {
    int x;
    S(): x(0) {} 
};

class C
{
    int a;
    int b;
    public:
    C(int i, int j){};
};
C c {0,0}; //C++11 only. 相当于 C c(0,0);

int* a = new int[3] { 1, 2, 0 }; // C++11 only
class X {
    int a[4];
    public:
    X() : a{1,2,3,4} {} //C++11, 初始化数组成员
};

int main(int argc, char** arg) {
    {
        std::string s("hello");
        int m=int();
    }
    {
        std::string s="hello";
        int x=5;
    }
    {
        int arr[4]={0,1,2,3};
        struct tm today={0};
    }
}

