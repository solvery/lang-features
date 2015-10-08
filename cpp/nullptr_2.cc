// c++11

#include <iostream>
#include <algorithm>
#include <numeric>
#include <string>
#include <vector>

using namespace std;

int main(int argc, char** arg) {
    string str;
    const char *pc=str.c_str(); //data pointers
    if (pc!=nullptr)
        cout<<pc<<endl;
}

