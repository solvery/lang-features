// 模板的模板参数

#include <iostream>
using namespace std;

/// template <template <typename T> typename U>
template <template <typename T> class U>
class A
{
};

int main(int argc, char** arg) {
}

