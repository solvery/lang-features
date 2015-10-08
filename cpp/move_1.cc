// c++11
// 右值引用

#include <iostream>
#include <algorithm>
#include <numeric>
#include <string>
#include <vector>

using namespace std;

class Movable
{
    Movable (Movable&&); //move constructor
    Movable&& operator=(Movable&&); //move assignment operator
};

int main(int argc, char** arg) {
}

