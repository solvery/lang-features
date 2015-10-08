// c++11

#include <iostream>
#include <algorithm>
#include <numeric>
#include <string>
#include <vector>

using namespace std;

void foo(int){
    cout << __func__ << 1 <<endl;
};
void foo(char *){
    cout << __func__ << 2 <<endl;
};

int main(int argc, char** arg) {
    //C++03
    foo(0); 
    //C++11
    foo(nullptr);
}

