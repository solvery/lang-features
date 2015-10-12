//  一个模板类继承另外一个模板类

#include <iostream>

using namespace std;

template <typename T>
class A {
};

template <typename T>
class B : public A<T> {
};

int main(int argc, char** arg) {
}



