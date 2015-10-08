
#include <vector>
#include <iostream>
using namespace std;

void func(const vector<int> &vi)
{
    vector<int>::const_iterator ci=vi.begin();
    auto ci2=vi.begin(); // 自动类型推导, 更简化
}

int main(int argc, char** arg) {
    // 自动类型推导
    auto x=0; 
    auto c='a'; 
    auto d=0.5; 
    auto national_debt=14400000000000LL;
}

