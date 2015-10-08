// c++11

#include <iostream>
#include <algorithm>
#include <numeric>
#include <string>
#include <vector>

using namespace std;

class M //C++11 delegating constructors
{
    int x, y;
    char *p;
    public:
    M(int v) : x(v), y(0),  p(new char [MAX])  {} //#1 target
    M(): M(0) {cout<<"delegating ctor"<<end;} //#2 delegating
};

int main(int argc, char** arg) {
}

