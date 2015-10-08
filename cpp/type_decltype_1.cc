#include <iostream>
#include <algorithm>
#include <numeric>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char** arg) {
    const vector<int> vi;
    // decltype 从一个表达式中“俘获”其结果的类型并“返回”
    typedef decltype (vi.begin()) CIT;
    CIT another_const_iterator;
}

