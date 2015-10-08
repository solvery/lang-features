// c++11
// default 指示编译器生成函数的默认实现

#include <iostream>
#include <algorithm>
#include <numeric>
#include <string>
#include <vector>

using namespace std;

struct A
{
    A()=default; //C++11
    virtual ~A()=default; //C++11
};

int main(int argc, char** arg) {
}

