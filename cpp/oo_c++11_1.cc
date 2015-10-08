// c++11

#include <iostream>
#include <algorithm>
#include <numeric>
#include <string>
#include <vector>

using namespace std;

class A {
    public:
        A(): A(2) {
            A(1);   // 构造函数可以调用同一个类的另一个构造函数, 委托构造函数
        }
        A(int a) {
        }
};

int main(int argc, char** arg) {
}

